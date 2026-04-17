[根目录](../CLAUDE.md) > **other**

# other 模块文档

## 变更记录 (Changelog)

- 2026-04-16 18:56:57：按 `/zcf/init-project` 更新脚本分层与高信号文件索引。

## 模块职责

`other` 是混合脚本集合，承载品牌活动、签到、抽奖与杂项自动化任务。

## 入口与启动

- Python 脚本入口：如 `tuchong.py`、`yuyun.py`、`七猫抽奖领宝箱.py`
- JavaScript 脚本入口：如 `sangsi.js`、`xj.js`、`百事乐元.js`
- 启动方式：按单脚本独立执行

## 对外接口

- 无统一 Web API
- 以“环境变量 + HTTP 请求 + 控制台日志”作为事实接口
- 部分脚本遵循类封装（如 `TuChong`, `RainYun`, `HgSp`）

## 关键依赖与配置

- Python 常见依赖：`requests`, `Crypto.Cipher.AES`
- JS 侧脚本通常依赖青龙 `Env` 范式和通知组件
- 环境变量信号：
  - `Tcck`（`tuchong.py`）
  - 各脚本自定义 `Authorization/cookie` 变量

## 数据模型

- 以第三方接口 JSON 响应为主，无本地统一 schema
- 多账号常见分隔策略：`&`、换行、`#`

## 测试与质量

- 未发现标准化 `tests/` 或统一测试框架
- 质量缺口：脚本命名与参数规范不一致，回归成本高

## 常见问题 (FAQ)

- Q: 为什么同类脚本风格差异较大？
  - A: 历史来源多、维护者多，形成“单脚本自治”模式。
- Q: 如何先做低风险治理？
  - A: 先统一环境变量解析与日志前缀，再逐步抽公共请求逻辑。

## 相关文件清单

- `tuchong.py`
- `yuyun.py`
- `七猫抽奖+转盘.py`
- `七猫抽奖领宝箱.py`
- `wx朵茜情调生活馆_jm.py`
- `xj.js`

