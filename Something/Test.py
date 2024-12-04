from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 使用 Service 创建 WebDriver
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
url = r'http://172.102.13.18:10000/'
driver.get(url)

wait = WebDriverWait(driver, 10)  # 最长等待 10 秒
input_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div[2]/div[2]/div/div[3]/input')))
input_element.send_keys('Selfpos.gzm_test1')




# driver.quit()
