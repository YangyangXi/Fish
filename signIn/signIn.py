import pickle
import requests
import time
import json
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")  # 禁止弹出通知
chrome_options.add_argument("--disable-popup-blocking") # 禁止弹出窗口拦截
# 启动Chrome浏览器
driver = webdriver.Chrome(service=Service(r"D:\python\chromedriver.exe"), options=chrome_options)
# driver.get(r'https://www.bilibili.com/')
driver.maximize_window()
driver.implicitly_wait(5)

# time.sleep(60)
# cookies = driver.get_cookies()
#
# # 保存cookies到json文件
# with open('cookies.json', 'w') as file:
#     json.dump(cookies, file)
#


def load_cookies_from_file(filename):
    with open(filename, 'r') as file:
        cookies = json.load(file)
        return cookies


loaded_cookies = load_cookies_from_file('cookies.json')
session = requests.Session()
for cookie in loaded_cookies:
    session.cookies.set(cookie['name'], cookie['value'])


# 发送带有cookies的请求
response = session.get(r'https://www.bilibili.com/')

# 输出响应内容
print(response.text)
time.sleep(10)


# xpath = "//img[@class='mhy-img-icon close']"
# element = driver.find_element(by=By.XPATH, value=xpath).click()
#
# xpath = "//img[@src='https://bbs-static.miyoushe.com/avatar/avatarDefaultPc.png']"
# element = driver.find_element(by=By.XPATH, value=xpath).click()
#
# xpath = '//*[@id="tab-password"]/text()'
# element = driver.find_element(by=By.XPATH, value=xpath).click()
#
# xpath = '//*[@id="username"]'
# element = driver.find_element(by=By.XPATH, value=xpath).send_keys('14777311972')
#
# xpath = '//*[@id="password"]'
# element = driver.find_element(by=By.XPATH, value=xpath).send_keys('zzpamlm1314')
#
# xpath = '//*[@id="app"]/div/div/form/label/span[1]/span'
# element = driver.find_element(by=By.XPATH, value=xpath).click()

# time.sleep(60)
#
#
#
#
# async def get_cookie():
#     try:
#         response = requests.get('https://www.baidu.com/cookie')
#         response.raise_for_status()
#         cookies = json.loads(response.content)
#         cookies = '; '.join(['='.join([key, value]) for key, value in cookies.items()])
#         print(cookies)
#         return cookies
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return None
#
# async def main():
#     await get_cookie()
#
#
# if __name__ == '__main__':
#
# # for i in range(0,6):
# #     xpath = f'//*[@id="__layout"]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div[{i}]/div[2]/div[2]/div/div/svg/use'
# #     element = driver.find_element(by=By.XPATH, value=xpath).click()
#
#     time.sleep(10)


