import sqlite3


conn = sqlite3.connect('../case03/demo.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO Employee(ID,NAME,AGE,ADDRESS,SALARY) "
               "VALUES (1,'Anika','Taipei',25,45000.0)")  # 執行 sql 語句
cursor.execute("INSERT INTO Employee(ID,NAME,AGE,ADDRESS,SALARY) "
               "VALUES (2,'John','Taoyuan',32,38000.0)")  # 執行 sql 語句
cursor.execute("INSERT INTO Employee(ID,NAME,AGE,ADDRESS,SALARY) "
               "VALUES (3,'Macy','Taipei',28,48000.0)")  # 執行 sql 語句
cursor.execute("INSERT INTO Employee(ID,NAME,AGE,ADDRESS,SALARY) "
               "VALUES (4,'Eason','NEW-Taipei',36,55000.0)")  # 執行 sql 語句
cursor.execute("INSERT INTO Employee(ID,NAME,AGE,ADDRESS,SALARY) "
               "VALUES (5,'Cathy','Taoyuan',29,32000.0)")  # 執行 sql 語句
cursor.execute("INSERT INTO Employee(ID,NAME,AGE,ADDRESS,SALARY) "
               "VALUES (6,'Joe','Taipei',22,35000.0)")  # 執行 sql 語句

conn.commit()  # 執行資料更新
conn.close()
print('完成')