'''
+-----------------+
| ___3___   傳送   |
| 766,20.50,52.00 |
+-----------------+
'''
import tkinter
import serial
import threading
from tkinter import font

COM_PORT = 'COM3'  # 指定通訊埠名稱
BAUD_RATES = 9600  # 設定傳輸速率(鮑率)
play = True

def receiveData():

    while play:
        try:
            global ser
            data_row = ser.readline()  # 讀取一行(含換行符號\r\n)原始資料
            data = data_row.decode()  # 預設是用 UTF-8 解碼
            data = data.strip("\r").strip("\n")  # 除去換行符號
            print(data)
            respText.set(data)
            try :
                values = data.split(",")
                cdsValue.set(values[0])
                tempValue.set(values[1])
                humiValue.set(values[2])
            except:
                pass

        except Exception as e:
            print("Serial closed ...", e)
            respText.set("Serial closed")

            # re-try
            try:
                ser = serial.Serial(COM_PORT, BAUD_RATES)
            except Exception as e:
                print("Serial exception: ", e)

            #break

def sendData(n):
    data_row = n + "#" # "#" 代表結束符號
    data = data_row.encode()
    ser.write(data)
    print("send: ", data_row, data)


if __name__ == '__main__':

    try:
        ser = serial.Serial(COM_PORT, BAUD_RATES)
    except Exception as e:
        print("Serial exception: ", e)

    root = tkinter.Tk()
    root.geometry("600x400")
    root.title("Arduino GUI")

    myfont1 =font.Font(family='Helvetica',size=36,weight='bold')
    myfont2 = font.Font(family='Helvetica', size=24)

    respText = tkinter.StringVar()
    respText.set("0,0.0,0.0")

    cdsValue = tkinter.StringVar()
    cdsValue.set("0")

    tempValue = tkinter.StringVar()
    tempValue.set("00.00")

    humiValue = tkinter.StringVar()
    humiValue.set("00.00")

    sendButton0  = tkinter.Button(text='0', command=lambda: sendData('0'),font=myfont2)
    sendButton1  = tkinter.Button(text='1', command=lambda: sendData('1'),font=myfont2)
    sendButton2  = tkinter.Button(text='2', command=lambda: sendData('2'),font=myfont2)
    sendButton3  = tkinter.Button(text='3', command=lambda: sendData('3'),font=myfont2)
    sendButton4  = tkinter.Button(text='4', command=lambda: sendData('4'),font=myfont2)
    sendButton8  = tkinter.Button(text='8', command=lambda: sendData('8'),font=myfont2)
    receiveLabel = tkinter.Label(root, textvariable=respText)
    cdsLabel = tkinter.Label(root, textvariable=cdsValue,font=myfont1,fg='#ff0000')
    tempLabel = tkinter.Label(root, textvariable=tempValue,font=myfont1,fg='#005100')
    humiLabel = tkinter.Label(root, textvariable=humiValue,font=myfont1,fg='#00f')

    root.rowconfigure((0,1), weight=1) # 列 0, 列 1 同步放大縮小
    root.columnconfigure((0,1,2,3,4,5), weight=1) # 欄 0, 欄 1, 欄 2 ...同步放大縮小

    sendButton0.grid(row=0,   column=0, columnspan=1, sticky='EWNS')
    sendButton1.grid(row=0,   column=1, columnspan=1, sticky='EWNS')
    sendButton2.grid(row=0,   column=2, columnspan=1, sticky='EWNS')
    sendButton3.grid(row=0,   column=3, columnspan=1, sticky='EWNS')
    sendButton4.grid(row=0,   column=4, columnspan=1, sticky='EWNS')
    sendButton8.grid(row=0,   column=5, columnspan=1, sticky='EWNS')
    cdsLabel.grid(row=1,  column=0, columnspan=2, sticky='EWNS')
    tempLabel.grid(row=1, column=2, columnspan=2, sticky='EWNS')
    humiLabel.grid(row=1, column=4, columnspan=2, sticky='EWNS')
    receiveLabel.grid(row=2,  column=0, columnspan=6, sticky='EWNS')

    t1 = threading.Thread(target=receiveData)
    t1.start()

    root.mainloop()
