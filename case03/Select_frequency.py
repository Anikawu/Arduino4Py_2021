# 哪一個數字出現最多 ?
import sqlite3
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

map = {}
for i in range(1, 40):
    map[i] = 0
print(map)

# 查詢資料列 sql
sql = 'SELECT id, n1, n2, n3, n4, n5, ts FROM Lotto'
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)

for r in rows:
    for i in range(1, 6):
        map[r[i]] = map[r[i]] + 1

print(map)
maxValue = max(map.values())
minValue = min(map.values())
print("max:", maxValue)
print("min:", minValue)

for k, v in map.items():
    if(v == maxValue):
        print("%d(%d)"%(k, maxValue))
    if (v == minValue):
        print("%d(%d)" % (k, minValue))

cursor.close()