from selenium import webdriver
import os
import json
import time


def browser_initial():
    """"
    进行浏览器初始化
    """
    os.chdir(os.path.dirname(os.path.dirname(__file__)))
    browser = webdriver.Chrome()
    goal_url = 'https://www.bilibili.com/'
    # 未携带cookies打开网页
    browser.get('https://www.bilibili.com/')
    return goal_url, browser


def log_taobao(goal_url, browser):
    """
    从本地读取cookies并登录目标网页
    """
    # 从本地读取cookies
    cookies_file_path = os.path.join(os.path.dirname(__file__), 'cookies', 'bilibili_cookies.txt')
    with open(cookies_file_path, 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())

    for cookie in listCookies:
        cookie_dict = {
            'domain': '.bilibili.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            'path': '/',
            "expires": '',
            'sameSite': 'Lax',
            'secure': cookie.get('secure')
        }
        browser.add_cookie(cookie_dict)

    # 更新cookies后进入目标网页
    browser.get(goal_url)


if __name__ == '__main__':
    tur = browser_initial()
    log_taobao(tur[0], tur[1])
    time.sleep(30)

