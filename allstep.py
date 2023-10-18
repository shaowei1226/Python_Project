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
import logging




driver = webdriver.Chrome()
driver.maximize_window()



url = "https://e02.efctw.com/"
driver.get(url)

logging.basicConfig(level=logging.WARNING)
username_field = driver.find_element(By.NAME,"uid")  
password_field = driver.find_element(By.NAME,"pwd")  
login_button = driver.find_element(By.ID,"button")  
username_field.send_keys("E2022054")
password_field.send_keys("H125406999")
login_button.click()
# 使用JavaScript打开新标签页
driver.execute_script("window.open('', '_blank');")


driver.switch_to.window(driver.window_handles[-1])
url2 = "https://e01.efctw.com/servlet/jform?file=efcbpm.dat"
driver.get(url2)
username_field = driver.find_element(By.NAME,"uid")  
password_field = driver.find_element(By.NAME,"pwd")  
login_button = driver.find_element(By.ID,"button")  

username_field.send_keys("E2022054")
password_field.send_keys("H125406999")
login_button.click()




button_element = driver.find_element(By.XPATH,"//li[@class='lv1']//span[contains(text(), '報工系統')]")
button_element.click()
time.sleep(1)  
button_element = driver.find_element(By.XPATH,"//li[@class='lv2']//span[contains(text(), '報工明細查詢-個人(WMPT5)')]")
button_element.click()
time.sleep(1) 

button_element = driver.find_element(By.XPATH,"//button[@class='dt-button buttons-excel buttons-html5']")
button_element.click()

time.sleep(15)  


# 取得今天的日期和時間
now = datetime.now()
date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

# 讀取Excel檔案
input_file = r'D:\Users\shaowei.zheng\Downloads\EFC 企業入口-報工明細查詢-個人(WMPT5).xlsx'
sheet_name = 'Sheet1'  #工作表名稱
df = pd.read_excel(input_file, sheet_name=sheet_name)
n_col_index = 13  
row_index = 1 


data_to_sum = df.iloc[row_index:, n_col_index]

sum_result = 0
ccc=0
ddd=0
for data in data_to_sum :
    sum_result+=data
    if data > 0:
     ccc+=1
    if data > 2:
     ddd+=1

#print(data_to_sum)
print(f'加班時數{sum_result}')
print(f'加班天數{ccc}')
print(f'加班大於2小時天數{ddd}')
nensalary = int(input("請輸入薪水"))
stopwork = int(input("請輸入請假天數"))
adsalary = 0
salary=0
adsalary = (ccc*2*((nensalary/30)/8))*1.34
workhetal=1916
bounty=170
print(f'勞健保{workhetal}')
print(f'福利金{bounty}')
salary=((sum_result-ccc*2)*1.67*((nensalary/30)/8))+adsalary+nensalary-workhetal-bounty-stopwork*(nensalary/30)
print(salary)

output_file = fr'C:\test\{date_time}.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_result = pd.DataFrame({"SUM": [salary]}) 
 
    df_result.to_excel(writer, index=False,startrow=0, startcol=0) 

print(f'新增 {output_file}')

try:
    os.remove(input_file)
    print(f"File '{input_file}' 已刪除.")
except FileNotFoundError:
    print(f"File '{input_file}' 沒找到.")
except Exception as e:
    print(f"An error occurred: {e}")