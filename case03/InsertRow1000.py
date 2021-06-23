import sqlite3
import random

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
lottos=[]  #建立一組陣列
for i in range(1000):
    #取出1-39不重複的數字 5個
    nums= set()
    while len(nums) <5:
        n=random.randint(1,39)
        nums.add(n)
    lottos.append(tuple(nums))  #轉成元組型的陣列()
    #元組陣列不可修改元素值

sql = 'INSERT INTO Lotto(n1, n2, n3, n4, n5) ' \
      'VALUES (?, ?, ?, ?, ?)'

cursor.executemany(sql,lottos)
conn.commit()
conn.close()

print('完成')