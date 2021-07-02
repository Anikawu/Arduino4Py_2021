'''
幸福大廈共有1~7層樓
您現在在 1 樓。請問要去哪一樓(輸入 0 可離開電梯)？
'''
from time import sleep
current_floor = 1
print("幸福大廈共有1~7層樓")
while True:

    n =int(input('您現在在 %d 樓,請問要去哪一樓(輸入0可以出電梯)?\n>>' %current_floor))
    try:
        target_floor = int(n)
    except ValueError:
        print("格式錯誤")
        continue
    if n ==0:
        break
    if n == current_floor:
        continue
    if n < 1 or n >7:
        print("請輸入介於1-7層樓")
        continue

    if n < current_floor:
        print('電梯下樓')
        while n < current_floor:
            print(current_floor)
            current_floor=current_floor-1
            sleep(1)
        print(current_floor)

    else:
        while n > current_floor:
           print(current_floor)
           current_floor = current_floor+1
           sleep(1)
        print(current_floor)

