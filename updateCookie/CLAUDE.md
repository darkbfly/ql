# updateCookie 模块文档

> **导航**: [ql 项目根目录](../CLAUDE.md) > updateCookie 模块

## 模块概述

`updateCookie` 模块提供 Cookie 自动更新和管理工具，支持多种平台的 Cookie 获取和更新，包括京东、淘宝等主流电商平台。

## 模块结构

```
updateCookie/
├── server.py                     # FastAPI Web 服务器
├── updateCookie_JD.py            # 京东 Cookie 更新脚本
├── updateCookie_TextLoop.py      # 文本循环更新脚本
├── updateCookie_Util.py          # Cookie 更新工具函数
├── JDLogin.py                    # 京东登录处理
├── webio.py                      # Web IO 处理
├── listDialog.py                 # 列表对话框
├── test.py                       # 测试脚本
├── runServer.bat                 # 启动服务器脚本
├── run_playwright.bat            # Playwright 运行脚本
├── jd.bat                        # 京东相关批处理
├── config.json                   # 配置文件
├── envs.json                     # 环境变量配置
├── subscription.json             # 订阅配置
├── dependencies-nodejs.json      # Node.js 依赖配置
├── dependencies-python3.json     # Python 依赖配置
├── app.log                       # 应用日志
└── *.txt                         # Cookie 文件（按手机号和域名命名）
```

## 关键文件

### `server.py`

**功能**：基于 FastAPI 的 Web 服务器，提供 Cookie 更新的 HTTP API 接口。

**主要特性**：
- FastAPI Web 框架
- RESTful API 接口
- Cookie 文件管理
- 环境变量管理

**核心功能**：
1. **Cookie 管理**：`addEnv(file_path, name, value, run, taskName)` 函数
2. **列表选择**：`get_list_item_by_index(data_list)` 函数
3. **文件操作**：按手机号和域名管理 Cookie 文件

**API 接口**（推测）：
- `POST /update-cookie`：更新 Cookie
- `GET /cookies`：获取 Cookie 列表
- `POST /env`：添加环境变量

**依赖**：
- `fastapi`：Web 框架
- `uvicorn`：ASGI 服务器
- `click`：命令行接口
- `pydantic`：数据验证
- `updateCookie_Util`：工具模块

**使用方式**：
```bash
# 启动服务器
python server.py
# 或使用批处理
runServer.bat

# 使用 uvicorn 启动
uvicorn server:app --host 0.0.0.0 --port 8000
```

### `updateCookie_JD.py`

**功能**：京东 Cookie 更新脚本。

**说明**：专门处理京东平台的 Cookie 获取和更新。

### `JDLogin.py`

**功能**：京东登录处理模块。

**说明**：处理京东账号登录逻辑，可能使用 Playwright 或 Selenium 进行自动化登录。

### `updateCookie_TextLoop.py`

**功能**：文本循环更新脚本。

**说明**：可能用于批量处理多个 Cookie 的更新。

### `updateCookie_Util.py`

**功能**：Cookie 更新工具函数库。

**说明**：提供通用的 Cookie 处理函数，被其他模块引用。

### `webio.py`

**功能**：Web IO 处理模块。

**说明**：可能用于 Web 自动化相关的 IO 操作。

### `listDialog.py`

**功能**：列表对话框模块。

**说明**：可能用于显示选择列表的对话框。

## Cookie 文件命名规则

Cookie 文件按以下格式命名：
```
{手机号}-{域名}.txt
```

**示例**：
- `13055789923-JD.txt`：手机号 13055789923 的京东 Cookie
- `13055789923-api.pinduoduo.com.txt`：手机号 13055789923 的拼多多 API Cookie
- `13055789923-clubwx.hm.liby.com.cn.txt`：手机号 13055789923 的某品牌 Cookie

## 接口说明

### `addEnv(file_path, name, value, run, taskName)`

添加或更新环境变量（Cookie）。

**参数**：
- `file_path`: 文件路径（域名）
- `name`: 环境变量名称
- `value`: Cookie 值
- `run`: 是否运行（布尔值）
- `taskName`: 任务名称

**功能**：
- 如果文件不存在，创建新文件并写入内容
- 如果文件存在，比较内容是否相同，不同则更新
- 文件内容为 JSON 格式

### `get_list_item_by_index(data_list)`

根据索引从列表中选择项。

**参数**：
- `data_list`: 数据列表

**返回**：选中的列表项

## 使用场景

1. **Cookie 自动更新**：定期更新各类平台的 Cookie
2. **多账号管理**：支持多个手机号对应的 Cookie 管理
3. **批量处理**：批量更新多个平台的 Cookie
4. **Web 服务**：通过 Web API 提供 Cookie 更新服务

## 依赖关系

### 外部依赖

- **Web 框架**：`fastapi`, `uvicorn`
- **命令行工具**：`click`
- **数据验证**：`pydantic`
- **浏览器自动化**：可能使用 `playwright` 或 `selenium`

### 被依赖

- 可能被青龙面板调用
- 可能被其他自动化脚本使用

## 配置说明

### 配置文件

1. **config.json**：主配置文件
2. **envs.json**：环境变量配置
3. **subscription.json**：订阅配置
4. **dependencies-nodejs.json**：Node.js 依赖
5. **dependencies-python3.json**：Python 依赖

### 环境要求

1. **Python 版本**：Python 3.7+
2. **Node.js**：如果需要运行 Node.js 脚本
3. **浏览器**：如果使用 Playwright/Selenium，需要安装浏览器驱动

### 安装依赖

```bash
# Python 依赖
pip install fastapi uvicorn click pydantic playwright

# Node.js 依赖（如果需要）
npm install
```

## 注意事项

1. **Cookie 安全**：Cookie 文件包含敏感信息，需要妥善保管
2. **文件管理**：大量 Cookie 文件需要定期清理和归档
3. **登录稳定性**：自动化登录可能不稳定，需要人工干预
4. **反爬虫**：某些平台可能有反爬虫机制，需要谨慎使用
5. **法律合规**：Cookie 获取和使用需遵守相关法律法规

## 支持平台

根据 Cookie 文件命名，支持以下平台（部分）：
- 京东（JD）
- 拼多多（pinduoduo.com）
- 淘宝/天猫
- 各类品牌小程序和 H5 应用

## 下一步建议

1. **API 文档**：使用 FastAPI 自动生成 API 文档
2. **认证机制**：添加 API 认证，保护 Cookie 更新接口
3. **日志系统**：完善日志记录，便于问题排查
4. **错误处理**：添加完善的异常处理和重试机制
5. **Cookie 验证**：添加 Cookie 有效性验证
6. **批量操作**：优化批量 Cookie 更新性能
7. **Web UI**：考虑添加 Web 管理界面

---

*本文档由 `/zcf/init-project` 命令自动生成*

