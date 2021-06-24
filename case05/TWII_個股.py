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
data =list(filter(lambda l:len(l.split(','))==7, data )) #過濾
#print(data)  會變成一個list
data ="\n".join(data)  #透過\n來合併
df =pd.read_csv(StringIO(data)) #將列表丟到csv裡面
#df = df.drop(index=[21]) # 刪除指定列
df= df[df.columns[df.isnull().all() == False]] #刪除不必要的欄位

print(df.dtypes) #列出每個資料欄位的型態
#df = df.set_index('日期') #設定index
df =df.rename(columns={'殖利率(%)':'殖利率'})
df =df.rename(columns={'財報年/季':'財報年季'})
print(df)

#繪圖


plt.plot(df['日期'], df['本益比'])  # 繪製折線圖
plt.title('%s %s PE' % (date,symbol))
plt.show()
plt.plot(df['日期'], df['殖利率'])  # 繪製折線圖
plt.title('%s %s RATE'% (date,symbol))
plt.show()
plt.plot(df['日期'], df['股價淨值比'])  # 繪製折線圖
plt.title('%s %s PB'% (date,symbol))
plt.show()