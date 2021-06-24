import requests
import sqlite3

path = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20210623&selectType=ALL'
csv = requests.get(path).text
# "證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
csv = csv.replace('"1,', '"1')
csv = csv.replace('"2,', '"2')
csv = csv.replace('"3,', '"3')
csv = csv.replace('"', '')
csv = csv.replace('-', '-1')
rows = csv.split("\r\n")
# "1,040.00" 1760
print(len(rows))
stocks = []
for row in rows:
    list = row.split(',')
    if len(list) == 8 and list[0] != '證券代號':
        #print(list)
        list[2] = float(list[2])  # 殖利率(%)
        list[3] = int(list[3])    # 股利年度
        list[4] = float(list[4])  # 本益比
        list[5] = float(list[5])  # 股價淨值比
        list[7] = '2021-06-23'
        stocks.append(tuple(list))

print(stocks)

# 匯入資料庫

sql = '''
        insert into Stock(證券代號, 證券名稱, 殖利率, 股利年度, 本益比, 股價淨值比, 財報年季, ts) 
        values(?, ?, ?, ?, ?, ?, ?, ?)
      '''

conn = sqlite3.connect('twii.db')
cursor = conn.cursor()
cursor.executemany(sql, stocks)

conn.commit()
conn.close()
print('OK')