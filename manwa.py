import cloudscraper
import time
import random

# ================= 配置区 (请重新粘贴！) =================
accounts = [
    "这里填入第一个账号的完整Cookie...", 
    "这里填入第二个账号的完整Cookie..."
]

# ================= 核心代码 =================
def run_sign_in(cookie_str, index):
    # 🧹【关键修复】自动清除前后空格和换行符
    clean_cookie = cookie_str.strip()
    
    # 简单的检查
    if "passwd" not in clean_cookie:
        print(f"⚠️ [账号 {index}] 警告：Cookie 里好像没看到 passwd 字段，可能粘贴错了？")

    print(f"\n🚀 [账号 {index}] 正在启动任务...")
    
    # 模拟 Chrome 浏览器
    scraper = cloudscraper.create_scraper(
        browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False}
    )
    
    ucenter_url = "https://manwa.me/ucenter"
    welfare_url = "https://manwa.me/users/welfare"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://manwa.me/ucenter",
        "Origin": "https://manwa.me",
        "X-Requested-With": "XMLHttpRequest",
        # 使用清洗过的 Cookie
        "Cookie": clean_cookie  
    }

    try:
        # 1. 访问用户中心
        scraper.get(ucenter_url, headers=headers)
        
        # 随机等待 2-4 秒 (避免被服务器发现是脚本批量操作)
        time.sleep(random.randint(2, 4))

        # 2. 请求福利接口
        data = {"action": "point", "page": "1"}
        response = scraper.post(welfare_url, headers=headers, data=data)
        
        # 3. 结果判断
        if response.status_code == 200:
            if "login" in response.url or "用户登录" in response.text:
                print(f"❌ [账号 {index}] 失败：Cookie 依然无效。")
                print("   -> 请检查是否把旧的 Cookie 粘贴进来了？")
            elif "msg" in response.text:
                 # 打印一点点内容确认
                print(f"✅ [账号 {index}] 成功！服务器返回: {response.text[:50]}...")
        elif response.status_code == 403:
            print(f"🚫 [账号 {index}] 403 被拦截：请尝试切换手机热点。")
        else:
            print(f"⚠️ [账号 {index}] 状态码: {response.status_code}")

    except Exception as e:
        print(f"❌ [账号 {index}] 报错: {e}")

# ================= 主程序 =================
if __name__ == "__main__":
    print(f"📋 准备运行 {len(accounts)} 个账号")
    
    for i, cookie in enumerate(accounts, 1):
        if len(cookie) < 10: # 跳过空行
            continue
            
        run_sign_in(cookie, i)
        
        if i < len(accounts):
            print("⏳ 休息 5 秒，准备切换下一个账号...")
            time.sleep(5)
            
    input("\n所有账号运行完毕，按回车退出...")