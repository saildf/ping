from selenium import webdriver
import time
# 循环打开百度
url = "http://www.baidu.com"
driver = webdriver.Chrome(r"F:\PyCharm Community Edition 2019.2\bin\chromedriver.exe")  # chromedriver.exe的路径
driver.get(url)  # 打开网页
n = 10
while n > 0:
    driver.refresh()
    time.sleep(2)
