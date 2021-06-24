import requests
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']  #引用中文字體


symbol="2330"
date="20210624"
path="https://www.twse.com.tw/exchangeReport/BWIBBU?response=csv&date=%s&stockNo=%s" % (date,symbol)

csv =requests.get(path).text
#print(csv)
#"日期","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
data=csv.split('\r\n')
data =list(filter(lambda l:len(l.split(','))==7, data ))
#print(len(data))
data ="\n".join(data)
df =pd.read_csv(StringIO(data)) #將列表丟到csv裡面
print(data)
print(df.dtypes) #列出每個資料欄位的型態