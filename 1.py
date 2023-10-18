import pandas as pd
from datetime import datetime
import os

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
for data in data_to_sum :
    sum_result+=data
    if data > 0:
     ccc+=1

print(data_to_sum)
print(sum_result)
print(ccc)

adsalary = 0
salary=0
adsalary = (ccc*2*151)*1.34
salary=((sum_result-ccc*2)*1.67*151)+adsalary+36400
print(salary)

output_file = fr'C:\test\{date_time}.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_result = pd.DataFrame({"SUM": [salary]}) 
 
    df_result.to_excel(writer, index=False,startrow=0, startcol=0) #在outputfile新增工作表

print(output_file)

try:
    os.remove(input_file)
    print(f"File '{input_file}' 已刪除.")
except FileNotFoundError:
    print(f"File '{input_file}' 沒找到.")
except Exception as e:
    print(f"An error occurred: {e}")

