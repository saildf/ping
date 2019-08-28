# coding=utf-8 规范字符编码设置中文字符集
from selenium import webdriver
import time

url = "http://www.youtube.com"
driver = webdriver.Chrome(r"F:\PyCharm Community Edition 2019.2\bin\chromedriver.exe")  # chromedriver.exe的路径
driver.get(url)  # 打开网页
i = 0
for i in range(1000):
    driver.refresh()
    time.sleep(2)

