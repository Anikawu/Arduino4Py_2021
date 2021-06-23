import sqlite3

sql = '''
       CREATE TABLE Employee(
         ID      INT PRIMARY KEY   NOT NULL,
         NAME    VARCHAR (20)      NOT NULL,
         AGE     INT               NOT NULL,
         ADDRESS VARCHAR (50),
         SALARY  REAL              NOT NULL
       )
      '''
conn = sqlite3.connect('../case03/demo.db')
cursor = conn.cursor()
cursor.execute(sql)  # 執行 sql 語句

conn.commit()  # 執行資料更新
conn.close()
print('完成')