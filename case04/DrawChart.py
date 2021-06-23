import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('../case03/demo.db')
df = pd.read_sql_query("SELECT NAME, SALARY FROM Employee", con=conn)
print(df)

# 繪圖
#移動平均線 #window=2 (兩點算出一個移動平均值)
ma=df['SALARY'].rolling(window=2).mean()
print(ma)
plt.plot(df.NAME.values, df.SALARY.values, 'r.')  # 點紅點
plt.plot(df['NAME'], df['SALARY'])  # 繪製折線圖
plt.plot(df['NAME'], ma)  # 繪製移動平均線折線圖(股票用)
plt.xlabel('Name')
plt.xlabel('Salary')
plt.show()

conn.close()