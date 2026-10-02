from pathlib import Path
import importlib,sys,json,hashlib,itertools,re
pkg=importlib.import_module(sys.argv[1]);views=importlib.import_module(sys.argv[2]);root=Path(sys.argv[3]);result=[]
files=sorted([*root.rglob('*.idb'),*root.rglob('*.i64')])
for path in files:
 item={'file':str(path.relative_to(root)),'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
 try:
  with pkg.from_file(str(path)) as db:
   item['wordsize']=db.wordsize
   try:
    r=views.Root(db);item['root']={'version':r.version,'md5':r.md5,'version_string':r.version_string,'created':r.created.isoformat()}
   except Exception as e:item['root_error']=(type(e).__name__,str(e))
   try:
    segments=views.Segments(db).segments
    item['segments']=[{'key':key,**{name:getattr(value,name) for name in ('startEA','endEA','sclass','orgbase','align','comb','perm','bitness','flags','sel','type','color')}} for key,value in sorted(segments.items())]
   except Exception as e:item['segment_error']=(type(e).__name__,str(e))
   try:
    functions=views.Functions(db).functions;item['function_count']=len(functions)
    item['function_sample']=[(k,v.startEA,v.endEA,v.flags) for k,v in sorted(functions.items())[:64]]
   except Exception as e:item['function_error']=(type(e).__name__,str(e))
   try:
    api=pkg.IDAPython(db);item['address_bounds']=(api.idc.MinEA(),api.idc.MaxEA())
    item['function_addresses']=list(itertools.islice(api.idautils.Functions(),64))
    item['function_names']=[api.idc.GetFunctionName(a) for a in item['function_addresses']]
   except Exception as e:item['api_error']=(type(e).__name__,str(e))
 except Exception as e:item['error']=(type(e).__name__,str(e))
 result.append(item)
for raw in [b'',b'IDB',b'IDA0'+bytes(64),b'garbage'*64]:
 try:pkg.from_buffer(raw);item={'raw':raw.hex(),'error':None}
 except Exception as e:item={'raw':raw.hex(),'error':(type(e).__name__,str(e))}
 result.append(item)
print(re.sub(r'(?<=<memory at )0x[0-9a-f]+','<allocation>',json.dumps(result,sort_keys=True)))
