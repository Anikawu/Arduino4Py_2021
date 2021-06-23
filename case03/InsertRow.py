import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
sql = 'INSERT INTO Lotto(n1, n2, n3, n4, n5) ' \
      'VALUES (1, 3, 5, 7, 9)'

cursor.execute(sql)
id = cursor.lastrowid  # 取得最新 id
print(id)

conn.commit()
conn.close()

print('完成')