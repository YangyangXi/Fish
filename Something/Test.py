from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = ChromeDriverManager().install()
chrome_options = Options()
chrome_options.add_argument("--headless")
try:
    # 初始化 WebDriver
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    driver.get('https://baidu.com')

    print(driver.title)

except Exception as e:
    print(f"启动浏览器时发生错误：{e}")

finally:

    driver.quit()
