#!/usr/bin/env python3
"""Verify the current bounded parser, fixed source comparisons, and installation."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import venv
import zipfile

ROOT = Path(__file__).resolve().parent
WORK = ROOT / '.verification'
UPSTREAM = 'https://github.com/williballenthin/python-idb.git'
COMMIT = '5a313f27cf6200e2454eb08ef3b557227fc2e9d7'
VERSION = '1.0.2'
DOCUMENTS = ('README.md', 'ORIGIN.md', 'VALIDATION.md', 'DEFENSIVE_SCOPE.md', 'NAME_AUDIT.json', 'CURRENT_VALIDATION.json')


def run(command, **kwargs):
    print('+', ' '.join(map(str, command)), flush=True)
    return subprocess.run(list(map(str, command)), cwd=ROOT, check=True, **kwargs)


def source_audit():
    manifest = json.loads((ROOT / 'SOURCE_MANIFEST.json').read_text())
    runtime = {str(path.relative_to(ROOT)) for path in (ROOT / 'src').rglob('*.py')}
    assert runtime <= set(manifest['files']), 'Runtime file missing from source manifest'
    for relative, record in manifest['files'].items():
        path = ROOT / relative
        data = path.read_bytes()
        assert len(data) == record['bytes'] and hashlib.sha256(data).hexdigest() == record['sha256'], relative
        assert bool(path.stat().st_mode & 0o111) == record['executable'], relative + ' mode differs'
    recorded = json.loads((ROOT / '项目文档/CURRENT_VALIDATION.json').read_text())['runtime_sha256']
    assert recorded == {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in sorted(runtime)}, 'Runtime identity differs from validation record'
    return len(manifest['files'])


def baseline_checkout(path):
    if path is None:
        path = WORK / 'upstream'
        if not path.exists():
            run(['git', 'clone', '--quiet', UPSTREAM, path])
        if subprocess.check_output(['git', '-C', str(path), 'rev-parse', 'HEAD'], text=True).strip() != COMMIT:
            run(['git', '-C', path, 'checkout', '--quiet', '--detach', COMMIT])
    path = path.resolve()
    assert subprocess.check_output(['git', '-C', str(path), 'rev-parse', 'HEAD'], text=True).strip() == COMMIT
    run(['git', '-C', path, 'diff', '--exit-code', COMMIT, '--', 'idb'])
    return path


def observe(script, modules, baseline=None, dataset=None):
    environment = dict(os.environ, PYTHONPATH=str(baseline or ROOT / 'src'))
    args = [sys.executable, ROOT / 'checks' / script, *modules]
    if dataset is not None:
        args.append(dataset)
    return json.loads(run(args, env=environment, capture_output=True).stdout)


def compare_databases(baseline):
    old = observe('idb_observations.py', ['idb', 'idb.analysis'], baseline, ROOT / 'checks/data')
    new = observe('idb_observations.py', ['idbmeadow', 'idbmeadow.semantic_views'], dataset=ROOT / 'checks/data')
    assert len(old) == len(new) == 51
    assert old[:-4] == new[:-4], 'Ordinary database observations differ'
    assert len(old[:-4]) == 47 and all('error' not in item for item in new[:-4])
    expected = [
        ('error', 'unpack_from requires a buffer of at least 32 bytes for unpacking 2 bytes at offset 30 (actual buffer size is 0)', 'truncated or invalid database header'),
        ('error', 'unpack_from requires a buffer of at least 32 bytes for unpacking 2 bytes at offset 30 (actual buffer size is 3)', 'truncated or invalid database header'),
        ('RuntimeError', 'unexpected file signature: <memory at <allocation>>', 'unsupported database version'),
        ('RuntimeError', 'unexpected file signature: <memory at <allocation>>', 'unsupported database version'),
    ]
    for first, second, (old_kind, old_message, new_message) in zip(old[-4:], new[-4:], expected):
        assert first['raw'] == second['raw']
        assert first['error'] == [old_kind, old_message]
        assert second['error'] == ['IDBFormatError', new_message]
        assert set(first) == set(second) == {'raw', 'error'}
    return {'observations': 51, 'equal': 47, 'precisely_checked_error_changes': 4}


def compare_pages(baseline):
    old = observe('page_observations.py', ['idb.fileformat', 'idb.typeinf'], baseline)
    new = observe('page_observations.py', ['idbmeadow.database_pages', 'idbmeadow.type_records'])
    assert len(old) == len(new) == 98
    changed = []
    header_fixes = []
    page_fixes = []
    for first, second in zip(old, new):
        if first == second:
            continue
        if 'header' in first:
            assert first['header'] == second['header'] in (1, 5)
            assert first['validated'] == ['ValueError', 'unsupported version'] and second['validated'] is True
            assert {key: value for key, value in first.items() if key != 'validated'} == {key: value for key, value in second.items() if key != 'validated'}
            header_fixes.append(first['header'])
            continue
        if 'flag_pages' in first or 'name_pages' in first:
            assert {key: value for key, value in first.items() if key != 'end'} == {key: value for key, value in second.items() if key != 'end'}
            if 'flag_pages' in first:
                assert first['end'] == 24576 and second['end'] == 16384
                page_fixes.append(('flags', *first['flag_pages']))
            else:
                width, count = first['name_pages']
                assert first['end'] == 16384 and second['end'] == 8192 + width * count
                page_fixes.append(('names', width, count))
            continue
        assert set(first) == {'bucket', 'error'} and set(second) == {'bucket', 'end', 'defs'}
        assert first['bucket'] == second['bucket'] and first['bucket'][1] is True
        assert first['error'] == ['Exception', 'v_bytes field set to wrong length!']
        format, _, count = first['bucket']
        assert format in (17, 18) and count in (0, 1, 3)
        assert second['defs'] == [['name%d' % index, index + 1, '01', 'comment', 2] for index in range(count)]
        assert second['end'] == {0: 20, 1: 44, 3: 57}[count]
        changed.append((format, count))
    assert sorted(changed) == [(format, count) for format in (17, 18) for count in (0, 1, 3)]
    assert sorted(header_fixes) == [1, 5] and len(page_fixes) == 10 and len(set(page_fixes)) == 10
    return {'observations': 98, 'equal': 80, 'precisely_checked_compressed_bucket_fixes': 6, 'fixed_header_validation': 2, 'actual_consumed_page_ends': 10}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--audit-only', action='store_true')
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--runslow', action='store_true')
    parser.add_argument('--skip-tests', action='store_true', help='Reuse a separately recorded suite; does not claim a new test execution.')
    args = parser.parse_args()
    WORK.mkdir(exist_ok=True)
    result = {'project': 'IDBMeadow', 'source_files_verified': source_audit(), 'status': 'PASS'}
    if args.audit_only:
        print(json.dumps(result)); return
    result['naming_audit'] = json.loads(run([sys.executable, ROOT / 'checks/naming_audit.py'], capture_output=True).stdout)
    baseline = baseline_checkout(args.baseline)
    if not args.skip_tests:
        run([sys.executable, '-m', 'pytest', 'checks', '-q', *(['--runslow'] if args.runslow else [])], env=dict(os.environ, PYTHONPATH=str(ROOT / 'src')))
    result['test_execution'] = 'not repeated (--skip-tests)' if args.skip_tests else ('complete with slow cases' if args.runslow else 'default suite; slow cases explicitly skipped')
    result['database_comparison'] = compare_databases(baseline)
    result['page_comparison'] = compare_pages(baseline)
    shutil.rmtree(ROOT / 'build', ignore_errors=True)
    output = WORK / 'dist' / VERSION
    run([sys.executable, '-m', 'build', '--no-isolation', '--sdist', '--wheel', '--outdir', output])
    wheels = list(output.glob('*.whl')); sources = list(output.glob('*.tar.gz'))
    assert len(wheels) == len(sources) == 1
    with zipfile.ZipFile(wheels[0]) as archive:
        for source in (ROOT / 'src').rglob('*.py'):
            relative = str(source.relative_to(ROOT / 'src'))
            assert archive.read(relative) == source.read_bytes(), relative
        for document in DOCUMENTS:
            entries = [name for name in archive.namelist() if name.endswith('/share/IDBMeadow/' + document)]
            assert len(entries) == 1 and archive.read(entries[0]) == (ROOT / '项目文档' / document).read_bytes(), document
        licenses = [name for name in archive.namelist() if name.endswith('/LICENSE.txt')]
        assert len(licenses) == 1 and archive.read(licenses[0]) == (ROOT / 'LICENSE.txt').read_bytes()
    result['wheel_source_provenance_license_identity'] = 'PASS'
    with tarfile.open(sources[0]) as archive:
        for relative, record in json.loads((ROOT / 'SOURCE_MANIFEST.json').read_text())['files'].items():
            entries = [member for member in archive.getmembers() if member.isfile() and member.name.endswith('/' + relative)]
            assert len(entries) == 1 and archive.extractfile(entries[0]).read() == (ROOT / relative).read_bytes(), relative
            assert bool(entries[0].mode & 0o111) == record['executable'], relative
    result['source_distribution_identity'] = 'PASS'
    with tempfile.TemporaryDirectory(prefix='idbmeadow-consumer-') as directory:
        consumer = Path(directory)
        venv.EnvBuilder(with_pip=True).create(consumer)
        interpreter = consumer / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
        run([interpreter, '-I', '-m', 'pip', 'install', '--force-reinstall', '--disable-pip-version-check', wheels[0]])
        environment = dict(os.environ, PYTHONPATH='')
        consumed = run([interpreter, '-I', ROOT / 'checks/wheel_consumption.py', ROOT, 'IDBMeadow'], env=environment, capture_output=True)
        result['independent_wheel_consumer'] = json.loads(consumed.stdout)
    result['assets'] = [{'name': path.name, 'bytes': path.stat().st_size, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in (*wheels, *sources)]
    (WORK / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
