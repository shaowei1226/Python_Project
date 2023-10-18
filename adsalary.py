import pandas as pd

# 讀取Excel檔案
input_file = 'EFC 企業入口-報工明細查詢-個人(WMPT5).xlsx'
sheet_name = 'Sheet1'  # 請將'Sheet1'替換為您的工作表名稱
df = pd.read_excel(input_file, sheet_name=sheet_name)
n_col_index = 13  # 設定為您想要讀取的 N 列（索引從 0 開始，所以需要減 1）
row_index = 1  # 設定為您想要讀取的第 9 行（索引從 0 開始，所以第 9 行的索引為 8）


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
salary=((sum_result-ccc*2)*1.67*151)+adsalary
print(salary)