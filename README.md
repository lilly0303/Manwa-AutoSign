Markdown
# Manwa AutoSign (漫蛙自动签到脚本)

基于 Python 的 Web 协议逆向工程实战项目。本项目通过 TLS 指纹伪造和会话劫持技术，实现了对目标站点的自动化签到与积分查询。

## 特性 (Features)

* **WAF 绕过**: 集成 `cloudscraper`，完美绕过 Cloudflare 5秒盾防护。
* **多账号支持**: 支持配置无限个账号，自动队列执行。
* **风控规避**: 内置随机抖动 (Jitter) 延时，模拟真人操作频率。
* **隐私安全**: 本地运行，Cookie 数据不经由第三方服务器。

## 快速开始 (Quick Start)

### 1. 安装依赖
```bash
pip install -r requirements.txt

运行
2. 配置账号
打开脚本文件，在 accounts 列表中填入你的 Cookie：

Python
accounts = [
    "uid=12345; passwd=xxxx; PHPSESSID=xxxx...",
]
如何获取 Cookie?

浏览器打开目标网站并登录。

按 F12 打开开发者工具 -> 网络(Network)。

刷新页面，找到 ucenter 或 welfare 请求。

复制请求头中的 Cookie 完整字符串。

3. 运行
Bash
python manwa_auto.py
⚠️ 免责声明 (Disclaimer)
本项目仅供 Python 学习与逆向工程研究使用。

请勿用于商业用途或非法用途。

开发者不对因使用本项目产生的任何后果负责。
