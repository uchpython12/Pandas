import pandas as pd
import pathlib
import numpy as np
#如果傳入的 是xlsx 返回讀取xlsx  csv 返回讀取csv
def read_excel_or_csv(FileName): #讀取excel_or_csv
    path = pathlib.Path(FileName)
    if path.suffix==".xlsx":
        # print('xlsx:', path.suffix)
        return pd.read_excel(FileName)
    elif path.suffix==".csv":
        # print('csv:', path.suffix)
        return pd.read_csv(FileName)

#另存新檔 xlsx
read_excel_or_csv('Iris.xlsx').to_excel('Iris1.xlsx', sheet_name='sheet1',index=False) #改寫xlsx
#另存新檔 csv
read_excel_or_csv('Iris.xlsx').to_csv('Iris.csv',index=False) #改寫xlsx
#讀取Iris.csv
df_csv = read_excel_or_csv('Iris.csv')
# print(df_csv) #顯示表內容
# print(df_csv["SepalLengthCm"]) #顯示欄位SepalLengthCm
# print(df_csv["SepalLengthCm"].head(5))# 顯示 前面五筆
# print(df_csv["SepalLengthCm"][1:10]) #印出前面1~10筆
# print(df_csv[["SepalLengthCm","PetalLengthCm"]]) #顯示欄位SepalLengthCm,PetalLengthCm

# for i in df_csv["SepalLengthCm"]:
#     print(i)
print(df_csv.columns.tolist())
print("============  Pandas 轉 Numpy ======== ")
df_Numpy =df_csv.to_numpy()
# print(df_Numpy)

print("============ Numpy 轉 Pandas======== ")
df_Pandas = pd.DataFrame(df_Numpy, columns = df_csv.columns)  # Pandas 轉 Numpy 指定欄位名稱
# print(df_Pandas)

print("============ Pandas 轉 List======== ")
df_List=df_Pandas.values.tolist()  #Pandas 轉 List
# print(df_List)

df_List_單一欄位=df_Pandas["SepalWidthCm"].tolist() # 取單一欄位資料
# print(df_List_單一欄位)

print("============ List 轉 Pandas ======== ")
df_Pandas = pd.DataFrame(df_List)
# print(df_Pandas)
df_Pandas = pd.DataFrame(df_List, columns = df_csv.columns)  # Pandas 轉 Numpy 指定欄位名稱
# print(df_Pandas)

# #用於查看一些基本的統計詳細信息，例如數據幀的百分位數，均值，標準差等或一係列數值。
# print(df_Pandas.describe())

print("============ List 轉 Numpy ======== ")
df_numpy = np.array(df_List)
# print(df_numpy)
# print(type(df_numpy))

print("============ Numpy 轉  List ======== ")

df_List =df_numpy.tolist()

# print(df_List)
# print(type(df_List))
