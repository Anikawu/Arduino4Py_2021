#查出 n1+....+n5=40
#有哪些?

import sqlite3
#查詢資料列 sql
sql ='''
        select 'MAX' AS TYPE, name, max(salary) as SALARY from Employee
        UNION ALL
        select 'MIN' AS TYPE, name, min(salary) as SALARY from Employee
    '''
conn = sqlite3.connect('../case03/demo.db')
cursor= conn.cursor()
cursor.execute(sql)
rows=cursor.fetchall()
print(rows)


cursor.close()
