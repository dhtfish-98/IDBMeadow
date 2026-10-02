# IDBMeadow 防御用途与本轮复核范围

复核日期：2026-10-02。

## 实际防御用途

离线读取有权限持有的 IDB/I64，调查结构、类型、函数和其他分析元数据。

## 实际能力

解析库读取数据库，offline_tools 可导出数据；run_ida_script 会执行调用者指定的 Python 文件并安装本进程 IDAPython 接口，不是脚本沙箱。dump_scripts 可导出数据库保存的脚本，dump_user 可显示用户/许可证元数据。

## 当前检查

本轮核对数据库读取、script_environment 和 offline_tools 的执行/导出路径；保留 Apache-2.0 来源及 fixture 归属。既有有限/完整验证的版本、XFAIL 和耗时边界见 VALIDATION.md。

## 验证边界

只运行自己审核且获准运行的脚本；申请材料避免披露数据库内的个人或许可证信息。IDA 8/9 和所有畸形数据库未证明；当前轮没有再次跑历史慢速全量套件。

## 来源与 CVP

本项目的上游、固定提交和许可见 [ORIGIN.md](ORIGIN.md)。保留原作者与许可证；历史名称/模块重构和本轮 Codex 辅助维护均不代表申请人独立编写了上游算法。最新源码、历史包和实际运行结果须按各自提交分别核对。

[Anthropic 当前 CVP 说明](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet)以受到网络安全防护影响的合法防御双用途任务为依据。项目数量、改名、构建和 CI 不证明申请资格；实际授权、身份、组织和受限任务仍需真实证据。这里没有本轮申请结果，也不保证某个模型永不触发网络安全防护。
