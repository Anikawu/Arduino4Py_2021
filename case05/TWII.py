import requests


path='https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20210623&selectType=ALL'
csv = requests.get(path).text

#"證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季"

csv = csv.replace('"1,','"1') #整理資料->先把雙引號 去除
csv = csv.replace('"2,','"2') #整理資料->先把雙引號 去除
csv = csv.replace('"3,','"3') #整理資料->先把雙引號 去除
csv = csv.replace('"','') #整理資料->先把雙引號 去除
csv=csv.replace('-','-1') #-號 變成-1
rows=csv.split("\r\n") #\r\n標準斷行
#"1,040.00"  將雙引號裡面的逗號拿掉
print(len(rows))  #查詢有幾列資料
#建立資料庫
stocks=[] #建立一個陣列
for row in rows:
    list = row.split(',')
    if len(list)==8 and list[0] !='證券代號':
        #print(list)
        list[2] = float(list[2]) #殖利率(%)
        list[3] = int(list[3]) #股利年度
        list[4] = float(list[4]) #本益比
        list[5] = float(list[5]) #股價淨值比
        stocks.append(tuple(list)) #將list存到陣列
print(stocks)

