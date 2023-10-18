from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui# 必要每五秒檢元素是否存在
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import pandas as pd
import requests
import os
import shutil


# 创建Chrome WebDriver对象
driver = webdriver.Chrome()
driver.maximize_window()


# 打开特定网页
url = "https://e02.efctw.com/"
driver.get(url)

# 查找登录表单元素并输入账号密码
username_field = driver.find_element(By.NAME,"uid")  # 使用实际网页上的元素ID
password_field = driver.find_element(By.NAME,"pwd")  # 使用实际网页上的元素ID
login_button = driver.find_element(By.ID,"button")  # 使用实际网页上的元素ID
username_field.send_keys("E2022054")
password_field.send_keys("H125406999")
login_button.click()
# 使用JavaScript打开新标签页
driver.execute_script("window.open('', '_blank');")

# 切换到新标签页
driver.switch_to.window(driver.window_handles[-1])
url2 = "https://e01.efctw.com/servlet/jform?file=efcbpm.dat"
driver.get(url2)
username_field = driver.find_element(By.NAME,"uid")  # 使用实际网页上的元素ID
password_field = driver.find_element(By.NAME,"pwd")  # 使用实际网页上的元素ID
login_button = driver.find_element(By.ID,"button")  # 使用实际网页上的元素ID
username_field.send_keys("E2022054")
password_field.send_keys("H125406999")
login_button.click()
time.sleep(86400)