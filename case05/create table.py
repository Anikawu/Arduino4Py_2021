
import sqlite3


#建立一個table
#證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季"
sql='''
        create table if not exists Stock(
            id integer primary key autoincrement,
            證券代號  nvarchar(20),
            證券名稱  nvarchar(20),
            殖利率 real,
            股利年度 integer,
            本益比 real,
            股價淨值比 real,
            財報年季 nvarchar(10),
            ts  nvarchar(20)
        )
    '''

conn = sqlite3.connect('twii.db')
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
conn.close()