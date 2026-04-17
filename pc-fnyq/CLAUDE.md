[根目录](../CLAUDE.md) > **pc-fnyq**

# pc-fnyq 模块文档

## 变更记录 (Changelog)

- 2026-04-16 18:56:57：按 `/zcf/init-project` 更新自动化流程与函数索引。

## 模块职责

`pc-fnyq` 提供 Windows 图像识别自动化脚本，面向京东/淘宝等桌面端任务流。

## 入口与启动

- 主入口：`pc-fnyq.py`
- 工具库：`mytool.py`
- 启动方式：`python pc-fnyq.py`（可配合 bat 脚本）

## 对外接口

核心函数：

- `toggle_pause()`：切换暂停/恢复
- `点击图片中心(path, png, timeout)`：定位图片并点击
- `寻找是否存在(path, png, timeout)`：轮询判断目标图像
- `run_jd()` / `run_taobao()`：平台流程驱动

## 关键依赖与配置

- 依赖：`pyautogui`, `keyboard`, `win32gui`, `win32con`
- 平台要求：Windows（Win32 API）
- 资源依赖：同目录及 `pc-asm/` 下 PNG 模板

## 数据模型

- 以屏幕图像匹配结果为核心状态，不维护数据库或结构化本地存储
- 运行状态变量：`bPuase`（暂停控制）

## 测试与质量

- 可见测试信号：历史 `test.py`（本轮未读取）
- 质量缺口：缺少图像匹配回归集与分辨率兼容矩阵

## 常见问题 (FAQ)

- Q: 为什么脚本在不同分辨率下不稳定？
  - A: 图片模板与窗口尺寸耦合，需匹配分辨率或提供多模板。
- Q: 拖动验证码失败率高怎么办？
  - A: 先校准 `confidence` 与拖动轨迹参数，再扩展重试策略。

## 相关文件清单

- `pc-fnyq.py`
- `mytool.py`
- `test.py`（历史信号）

