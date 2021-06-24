import requests
symbol="2330"
date="20210624"
path="https://www.twse.com.tw/exchangeReport/BWIBBU?response=csv&date=%s&stockNo=%s" % (date,symbol)

csv =requests.get(path)
print(csv.text)