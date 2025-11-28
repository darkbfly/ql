# other 模块文档

> **导航**: [ql 项目根目录](../CLAUDE.md) > other 模块

## 模块概述

`other` 模块包含各类杂项脚本和工具，包括 Node.js 项目、Python 脚本和 JavaScript 脚本，用于各种自动化任务。

## 模块结构

```
other/
├── package.json                  # Node.js 项目配置
├── node_modules/                 # Node.js 依赖
├── qimao.js                      # 七猫相关脚本
├── sangsi.js                     # 相关脚本
├── xj.js                         # 相关脚本
├── 拼多多果园.js                  # 拼多多果园脚本
├── 牙博士.js                      # 牙博士脚本
├── 百事乐元.js                    # 百事乐元脚本
├── 七猫抽奖+转盘.py               # 七猫抽奖脚本
├── 七猫抽奖领宝箱.py              # 七猫抽奖脚本
├── tuchong.py                    # 图虫相关脚本
├── qt.py                         # 相关脚本
├── yuyun.py                      # 相关脚本
├── 派勇.py                        # 派勇脚本
├── 蒙牛营养生活家.py               # 蒙牛营养生活家脚本
├── 火锅视频修复加强.py             # 火锅视频修复脚本
├── wx朵茜情调生活馆_jm.py         # 微信小程序脚本
├── 财富牛子.py                    # 财富牛子脚本
├── curlDown.bat                  # 下载脚本
├── pdd.1bat                      # 拼多多相关脚本
├── pdd.log                       # 日志文件
└── ...
```

## 关键文件

### `package.json`

**功能**：Node.js 项目配置文件。

**依赖**：
```json
{
  "dependencies": {
    "got": "^14.4.1",
    "request": "^2.88.2"
  }
}
```

**说明**：包含 HTTP 请求相关的 Node.js 依赖。

### `qimao.js`

**功能**：七猫相关自动化脚本（JavaScript 实现）。

### `拼多多果园.js`

**功能**：拼多多果园自动化脚本。

### `七猫抽奖+转盘.py` / `七猫抽奖领宝箱.py`

**功能**：七猫抽奖相关 Python 脚本。

### `tuchong.py`

**功能**：图虫相关 Python 脚本。

**依赖**（推测）：
- `base64`
- `hashlib`
- `requests`
- `Crypto.Cipher.AES`（加密解密）

### `蒙牛营养生活家.py`

**功能**：蒙牛营养生活家品牌签到/任务脚本。

### `火锅视频修复加强.py`

**功能**：火锅视频相关修复脚本。

### `wx朵茜情调生活馆_jm.py`

**功能**：微信小程序"朵茜情调生活馆"相关脚本。

### `财富牛子.py`

**功能**：财富牛子相关脚本。

## 接口说明

### Node.js 脚本接口

Node.js 脚本通常遵循以下模式：
```javascript
const $ = new Env("脚本名称");
let ckName = `cookie_name`;
let userCookie = checkEnv($.isNode() ? process.env[ckName] : $.getdata(ckName));
const notify = $.isNode() ? require("./sendNotify") : "";
```

### Python 脚本接口

Python 脚本可能使用：
- `ApiRequest` 类（来自根目录）
- `mytool` 工具函数
- `notify` 通知服务

## 使用场景

1. **品牌签到**：各类品牌应用的自动化签到任务
2. **抽奖活动**：参与各类抽奖和转盘活动
3. **视频处理**：视频相关修复和处理
4. **小程序自动化**：微信小程序相关任务

## 依赖关系

### Node.js 依赖

- `got`: HTTP 请求库（现代版本）
- `request`: HTTP 请求库（传统版本）

### Python 依赖

- 可能依赖根目录的 `ApiRequest.py`、`mytool.py`、`notify.py`
- 部分脚本可能需要 `Crypto` 库用于加密解密

## 配置说明

### Node.js 环境

1. 安装依赖：`npm install`（在 `other/` 目录下）
2. 配置环境变量：通过青龙面板或 `.env` 文件

### Python 环境

1. 确保根目录的工具模块可访问
2. 配置相应的 Cookie 环境变量

## 注意事项

1. **混合语言**：模块包含 Python 和 JavaScript 两种语言的脚本
2. **依赖管理**：Node.js 脚本需要单独安装依赖
3. **环境变量**：不同脚本可能使用不同的环境变量名称
4. **日志文件**：`pdd.log` 等日志文件可能包含敏感信息

## 脚本分类

### JavaScript 脚本

- `qimao.js`
- `sangsi.js`
- `xj.js`
- `拼多多果园.js`
- `牙博士.js`
- `百事乐元.js`

### Python 脚本

- `七猫抽奖+转盘.py`
- `七猫抽奖领宝箱.py`
- `tuchong.py`
- `qt.py`
- `yuyun.py`
- `派勇.py`
- `蒙牛营养生活家.py`
- `火锅视频修复加强.py`
- `wx朵茜情调生活馆_jm.py`
- `财富牛子.py`

### 批处理脚本

- `curlDown.bat`
- `pdd.1bat`

## 下一步建议

1. **代码整理**：按功能或品牌分类组织脚本
2. **依赖统一**：统一 Node.js 和 Python 的依赖管理
3. **文档完善**：为每个脚本添加使用说明
4. **错误处理**：统一错误处理和日志记录机制
5. **测试覆盖**：添加单元测试和集成测试

---

*本文档由 `/zcf/init-project` 命令自动生成*

