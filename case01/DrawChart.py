# -*- coding: UTF-8 -*-
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('iot.db')
df = pd.read_sql_query("SELECT id, cds, temp, humi, ts FROM Env "\
                       "order by ts desc limit 15", con=conn) #取最後50筆的資料

df = df[::-1] #reserve
print(df)

# 繪圖
#ma = df['SALARY'].rolling(window=2).mean()  # window=2 (二點算出一個平均值)移動平均值
#print(ma)
#plt.plot(df.ts.values, df.temp.values, 'r.')  # 點紅點
plt.plot(df['ts'], df['temp'], label="temp")  # 繪製折線圖
plt.plot(df['ts'], df['humi'], label="humi")  # 繪製折線圖
plt.grid(True) #加入格線
#plt.plot(df['NAME'], ma)  # 繪製移動平均線折線圖
# 圖例
plt.xlabel('time')
plt.ylabel('value(%)')
plt.xticks(rotation=90)#x軸資料轉90度
plt.legend() #圖利

plt.show()

conn.close()