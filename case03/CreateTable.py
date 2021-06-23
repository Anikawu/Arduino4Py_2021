import sqlite3

sql = 'create table if not exists Lotto(' \
      'id INTEGER PRIMARY KEY AUTOINCREMENT, '\
      'n1 INTEGER, ' \
      'n2 INTEGER, ' \
      'n3 INTEGER, ' \
      'n4 INTEGER, ' \
      'n5 INTEGER, ' \
      'ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)  # 執行 sql 語句

conn.commit()  # 執行資料更新
conn.close()
print('完成')