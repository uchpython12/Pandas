import pandas as pd
import numpy as np


def 空資料資料轉換(df1):
    print("-----方法1 空資料資料轉換------")

    print("移除掉空的資料前", df1.shape)
    print(df1)  # 移除掉空的資料前
    age_no_na = df1[df1.notna()]
    print("移除掉空的資料後",age_no_na.shape)
    print(age_no_na) #"移除掉空的資料"
    age_na1 = df1.isnull()
    print("空的資料",age_na1)
    age_na2 = df1.isnull().values.any()
    print("空的資料",age_na2)

def 補上0():
    print("-----方法2 補上0------")
    df2=df1.fillna(0)  #  如果是空的 補上0
    print(df2)

def 移除row():
    print("-----方法2  移除 row------")
    df3 = df1.dropna()
    print(df3)

def 移除col():
    print("-----方法3  移除 col------")
    df4 = df1.dropna(axis=1)
    print(df4)


def 補上平均值col():
    print("-----方法4  補上 平均值 col------")
    df5=df1
    mean1=df5["C"].mean()
    df5["C"]=df5["C"].fillna(mean1)
    print(df5)

df1 = pd.DataFrame([[1, 2, 3, 4],
                   [5, 6, np.nan, 8]],
                  columns=list("ABCD"))
# print(df1)
# 空資料資料轉換(df1)
# 補上0()
# 移除row()
# 移除col()
# 補上平均值col()


df1 = pd.DataFrame([[1, "YES", 3, 4],
                    [5, "YES", 7, 8],
                    [5, "No", 7, 8]],
                  columns=list("ABCD"))

def 文字轉數字():
    print("-----方法5  文字 轉 數字------")
    df1['E'] = df1['B'].rank(method='dense', ascending=False).astype(int)
    print (df1)
# 文字轉數字()
def 文字轉數字移除掉文字的欄位(df1):
    print("-----方法6  文字 轉 數字 移除掉文字的欄位------")
    df1=df1.drop(columns=['B'])
    print (df1)
# 文字轉數字移除掉文字的欄位(df1)

def 修改欄位名稱(df1):
    print("-----方法7  修改欄位名稱------")
    df1.columns = df1.columns.str.replace('B', 'E')
    # df1 = df1.rename(columns={'B': 'E'})
    print(df1)
# 修改欄位名稱(df1)
def 修改資料型態():
    print("-----方法8  修改資料型態------")
    print(df1.info())
    df1["A"]=df1["A"].astype(float)
    df1["B"]=df1["B"].astype(str)
    print(df1.info())
# 修改資料型態()

def 移除重複的row資料():
    print("-----方法9  移除重複的row資料------")
    df1 = pd.DataFrame([[1,2, 3, 4],
                        [5, 6, 7, 8],
                        [5, 6, 7, 8]],
                      columns=list("ABCD"))
    print("移除前")
    print(df1)
    df1=df1.drop_duplicates()
    print("移除後")
    print(df1)
# 移除重複的row資料()
def 移除重複的col欄位名稱的資料():
    print("-----方法10  移除重複的col欄位名稱的資料------")
    df1 = pd.DataFrame([[1, 2, 3, 13,   4],
                        [5, 6, 7, 17,   8],
                        [9, 10,11,11, 12]],
                      columns=list("ABCCE"))
    print("移除前")
    print(df1)
    df1 = df1.loc[:,~df1.columns.duplicated()].copy()
    print("移除後")
    print(df1)
# 移除重複的col欄位名稱的資料()

def 欄位名稱的不一樣字串():
    print("-----方法11  欄位名稱的不一樣 字串------")
    df1 = pd.DataFrame([["臺北市",  2, 3, 4],
                        ["台北市",  6, 7, 8],
                        ["taipei", 10,11,12],
                        [" TAIPEI ", 10,11,12],
                        ["Taipei", 10,11,12],
                        ],
                      columns=list("ABCD"))

    dict1={'臺北市':'taipei',
           '台北市':'taipei',
           }

    df1['A'] = df1['A'].replace(dict1) #替換文字
    df1['A'] = df1['A'].str.lower() #lower()方法返回所有基於大小寫的字符被轉換為小寫字符串
    df1['A'] = df1['A'].str.replace(" ","") #替換空白
    print(df1)
# 欄位名稱的不一樣字串()

def 找出有問題的資料():
    print("-----方法12  找出有問題的資料------")
    df1 = pd.DataFrame([["臺北市",  2, 3, 4],
                        ["台北市",  6, 7, 8],
                        ["北北市",  6, 7, 8],
                        ["taipei", 10,11,12],
                        [" TAIPEI ", 10,11,12],
                        ["TaipeJ", 10,11,12],
                        ],
                      columns=list("ABCD"))

    dict1={'臺北市':'taipei',
           '台北市':'taipei',
           }

    df1['A'] = df1['A'].replace(dict1)
    df1['A'] = df1['A'].str.lower()
    df1['A'] = df1['A'].str.replace(" ","")
    print(df1)
    df1.to_excel("debug.xlsx")
    df2=df1[df1['A']!="taipei"]
    print(df2)
找出有問題的資料()