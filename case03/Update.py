import sqlite3

sql ='UPDATE Lotto SET n1=%d,n2=%d WHERE id=%d' \
    %(39,38,1)
print(sql)

conn=sqlite3.connect("demo.db")
cursor = conn.cursor()
cursor.execute(sql)

print("Update ok,rowcunt",cursor.rowcount)
conn.commit()
conn.close()