'''
作業 (利用 lambda)
id = 'A123456789'
第二碼 sex  = id[1] -> 1 (1: 男, 2: 女)
第三碼 area = id[2] -> 2 (0~5: 台灣, 6: 外國, 7: 無戶籍, 8: 港澳, 9: 大陸)
印出: 台灣男
'''

id ="A123456789"
sex =id[1]
#print(sex)
area =id[2]
#print(area)

sex_info ={
    1:lambda: print("男"),
    2:lambda: print("女")
}
area_info={
     0: lambda : print("台灣"),
     1: lambda : print("台灣"),
     2: lambda : print("台灣"),
     3: lambda : print("台灣"),
     4: lambda : print("台灣"),
     5: lambda : print("台灣"),
     6: lambda :print("外國"),
     7: lambda :print("無戶籍"),
     8: lambda :print("港澳"),
     9: lambda :print("大陸")
}


area_info.get(int(area))()  #呼叫lambda的方法
sex_error = lambda : print("性別錯誤")
sex_info.get(int(sex),sex_error)()  #呼叫lambda的方法

