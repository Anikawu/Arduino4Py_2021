import serial  #引用pyserial 模組
import random
import time
#COM_PORT='COM3'  #指定通訊埠
COM_PORT='COM6'  #指定通訊埠
#COM_PORT='COM7'  #指定通訊埠
BAUD_RATES =9600 #設定傳輸速率
ser = None

try:
    ser = serial.Serial(COM_PORT, BAUD_RATES)  # 初始化通訊埠
    while True:
        #data_row = str(random.randint(0, 100)) + "#"  # "#"表示結束字元
        data_row = str(input('請輸入欲傳送的數字:')) + "#"
        data = data_row.encode()
        ser.write(data)
        print("send: ", data_row, data)
        time.sleep(0.5)

except serial.SerialException:
    print("通訊埠無法建立, 請確認:")
    print("1.通訊埠名稱")
    print("2.傳輸速率(鮑率)")
    print("3.是否有關閉 Arduino IDE 的序列埠通訊視窗")
    print("exit!")

except KeyboardInterrupt:
    if ser is not None:
        ser.close() # 關閉通訊埠
    print("bye!")

except:
    print('其他錯誤')