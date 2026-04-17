[根目录](../CLAUDE.md) > **updateCookie**

# updateCookie 模块文档

## 变更记录 (Changelog)

- 2026-04-16 18:56:57：按 `/zcf/init-project` 重建模块索引与关键接口梳理。

## 模块职责

`updateCookie` 负责抓包数据接收、Cookie 文件落盘、青龙环境变量同步与登录辅助。

## 入口与启动

- 主入口：`server.py`（`FastAPI` 应用）
- CLI/脚本入口：`JDLogin.py`、`webio.py`
- 工具层：`updateCookie_Util.py`、`updateCookie_TextLoop.py`

## 对外接口

- HTTP 路由集中于 `server.py`
  - 路由形式：`@app.post("/<host>")`
  - 请求体模型：`Buffer(BaseModel)`，包含 `headers/body/path/queries` 等
  - 核心行为：提取 header token 并通过 `addEnv()` 写入 `{phone}-{host}.txt`

## 关键依赖与配置

- Python 依赖：`fastapi`, `uvicorn`, `click`, `pydantic`, `playwright`, `pyperclip`
- 模块内依赖：`updateCookie_Util.py`（QL 登录、任务触发、环境变量读写）
- 配置信号：代码中读取 `config.json`（用于手机号列表等）

## 数据模型

- `Buffer`：API 入参载体（URL/Method/Host/Body/Headers/Queries/Context）
- Cookie 文件：JSON 结构，字段包含 `name/value/remark/run/taskName`

## 测试与质量

- 可见测试信号：历史上存在 `test.py`（本轮未深读）
- 质量缺口：缺少统一异常治理、接口契约测试与回归样例

## 常见问题 (FAQ)

- Q: 为什么会生成多个 `*.txt` Cookie 文件？
  - A: 按 `手机号-host` 维度做隔离落盘，避免多账号串值。
- Q: Token 更新后为什么任务未触发？
  - A: 需检查 `updateCookie_Util.py` 的 QL 登录配置与 task name 映射。

## 相关文件清单

- `server.py`
- `updateCookie_Util.py`
- `updateCookie_TextLoop.py`
- `JDLogin.py`
- `webio.py`
- `listDialog.py`

