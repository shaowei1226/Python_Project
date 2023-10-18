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
from selenium.webdriver.support.ui import Select
import shutil

# 创建Chrome WebDriver对象
#driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
# 打开特定网页
url = "https://accounts.google.com/signup/v2/createaccount?biz=true&cc=TW&continue=https%3A%2F%2Fwww.google.com%3Fhl%3Dzh-TW&dsh=S-1341182001%3A1695016895941664&flowEntry=SignUp&flowName=GlifWebSignIn&hl=zh-TW&theme=glif"
driver.get(url)

userlastname_field = driver.find_element(By.NAME,"lastName")  
userfirstname_field = driver.find_element(By.NAME,"firstName")  
login_button = driver.find_element(By.ID,"collectNameNext") 
userlastname_field.send_keys("Kevin")#最後名
userfirstname_field.send_keys("shao")#前面名
login_button.click()
time.sleep(2)
useryear_filed = driver.find_element(By.NAME,"year")
usermonth_filed = driver.find_element(By.ID,"month")
userday_filed = driver.find_element(By.NAME,"day")
gender_filed = driver.find_element(By.ID,"gender")
select = Select(gender_filed)
select.select_by_value("1")#選擇性別
useryear_filed.send_keys("1999")#出生年
usermonth_filed.send_keys("12")#出生月
userday_filed.send_keys("26")#出生日
birthday_button = driver.find_element(By.ID,"birthdaygenderNext")
birthday_button.click()
time.sleep(3)
account_choose_filed = driver.find_element(By.ID,"selectionc1")
account_choose_filed.click()
next_button = driver.find_element(By.ID,"next")
next_button.click()
time.sleep(3)
userpwd_filed = driver.find_element(By.NAME,"Passwd")
userpwdagain_filed = driver.find_element(By.NAME,"PasswdAgain")
con_filed = driver.find_element(By.ID,"createpasswordNext")
userpwd_filed.send_keys("C120129c3")
userpwdagain_filed.send_keys("C120129c3")
con_filed.click()
time.sleep(3)
#skip_button = driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d")
#skip_button.click()

#cellphone_button = driver.find_element(By.CLASS_NAME,"VfPpkd-RLmnJb")
#cellphone_button.click()

cellphone_Check = driver.find_element(By.ID,"phoneNumberId")
cellphone_Check.send_keys("0989570359")
time.sleep(5)
cellphone_Check_button = driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d")
cellphone_Check_button.click()
time.sleep(800)
