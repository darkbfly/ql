---
name: python-apirequest-style
description: 在本仓库编写 Python 自动化脚本时，优先复用 ApiRequest.py 的结构与执行模型。
---

# Python ApiRequest 风格（ql）

当你在 `ql` 仓库新增或修改 Python 业务脚本时，优先参考根目录 `ApiRequest.py`，保持以下模式一致。

## 适用场景

- 新增“按环境变量多账号循环执行”的脚本
- 需要统一请求会话、统一异常上报、统一通知出口的脚本
- 对接 `mytool.py`、`notify.py`、`wxpusher` 的自动化任务脚本

## 必须遵守的结构

1. **请求基类**
   - 提供类似 `ApiRequest` 的基础类，初始化时使用 `requests.session()`
   - 默认关闭证书告警（`urllib3.disable_warnings()`）
   - `session.verify = False`、`session.trust_env = False`
   - 预留通知字段（如 `title`、`sendmsg`）和发送方法（调用 `notify.send`）

2. **执行器类**
   - 提供类似 `ApiMain` 的统一入口类
   - 构造函数接收任务函数名列表（`funcName`）
   - `run(envName, request)` 负责：
     - 可选加载本地 `debug.py` 并设置调试环境
     - 从 `mytool.getlistCk(envName)` 获取账号列表
     - 校验环境变量为空时给出提示并终止
     - 双层循环：账号 × 任务函数
     - 使用 `getattr(request(i), func)()` 动态执行
     - 捕获异常并推送 `traceback.format_exc()`

3. **通知策略**
   - 常规消息走 `notify.send`
   - 异常消息通过 `wxpusher` 推送（依赖环境变量 `wxpusherTopicId`、`wxpusherAppToken`）
   - 异常同时 `traceback.print_exc()` 便于本地排查

## 编码约束（按现有仓库风格）

- 以“最小改动、最少抽象”为先，不引入与当前脚本无关的框架化封装
- 命名、流程和异常处理优先与 `ApiRequest.py` 对齐
- 涉及 Cookie、Token、手机号等敏感信息时，禁止明文打印
- 新脚本优先复用根层工具：`ApiRequest.py`、`mytool.py`、`notify.py`

## 推荐骨架

```python
from ApiRequest import ApiRequest, ApiMain


class Task(ApiRequest):
    def __init__(self, ck):
        super().__init__()
        self.ck = ck
        self.title = "任务标题"

    def do_task(self):
        # 业务逻辑
        pass


if __name__ == "__main__":
    ApiMain(["do_task"]).run("ENV_NAME", Task)
```

## 自检清单

- 是否复用了 `ApiRequest` + `ApiMain` 模式
- 是否通过 `mytool.getlistCk` 做多账号遍历
- 是否具备异常捕获 + wxpusher 推送
- 是否避免输出敏感信息
- 是否保持仓库现有脚本风格（不过度抽象）
