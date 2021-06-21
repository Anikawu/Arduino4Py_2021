import serial  #引用pyserial 模組

COM_PORT='COM3'  #指定通訊埠
BAUD_RATES =9600 #設定傳輸速率
ser = None

try:
    ser = serial.Serial(COM_PORT,BAUD_RATES) #初始化通訊埠

    while True:
        while ser.in_waiting: #若有收到序列資料(相當於 arduino的Serial.available)
            data_row = ser.readline()  #讀取一行資料(含換行符號\r\n)原始資料
            data = data_row.decode()  #預設是用UTF-8 解碼
            data = data.strip("\r").strip("\n")  #除去段行符號
            print(data)

except serial.SerialException:
      print("通訊埠無法建立,請確認:")
      print("1.通訊埠名稱")
      print("2.傳輸速率(鮑率)")
      print("3.使否有關閉 arduino IDE 的序列埠視窗")
      print("exit!!")
except KeyboardInterrupt:
    if ser is not None:
        ser.close()  # 關閉通訊埠
    print("bye!")
except:
    print("其他錯誤")