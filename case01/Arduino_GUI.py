'''
+-----------------+
| ___3___   傳送   |
| 766,20.50,52.00 |
+-----------------+
'''
import tkinter
import serial
import threading
import case01.OPENWeather as ow
from tkinter import font
from io import BytesIO
from PIL import Image, ImageTk

COM_PORT = 'COM9'  # 指定通訊埠名稱
BAUD_RATES = 9600  # 設定傳輸速率(鮑率)
play = True
data=""
def receiveData():

    while play:
        try:
            global ser
            data_row = ser.readline()  # 讀取一行(含換行符號\r\n)原始資料
            global data
            data = data_row.decode()  # 預設是用 UTF-8 解碼
            data = data.strip("\r").strip("\n")  # 除去換行符號
            print(data)
            respText.set(data)
            try :
                values = data.split(",")
                cdsValue.set("%d lu" % (float(values[0])))
                tempValue.set("%.1f C" % (float(values[1])))
                humiValue.set("%.1f %%" % (float(values[2])))
                if(int(values[3]) == 16):
                    sendButton0.config(image=buzeer_open_photo)
                    sendButton0.image = buzeer_open_photo
                elif (int(values[3]) == 32):
                    sendButton0.config(image=buzeer_close_photo)
                    sendButton0.image = buzeer_close_photo

                if (int(values[4]) == 65): #65:關門狀態
                    sendButton4.config(image=door_close_photo)
                    sendButton4.image = door_close_photo
                elif (int(values[4]) == 165):

                    sendButton4.config(image=door_open_photo)
                    sendButton4.image = door_open_photo
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

def openTheDoor():
    door = int(data.split(",")[4])
    if door == 165 :
        sendData('8')
    elif door == 65:
        sendData('4')

def getOpenWeatherData():
    status_code, main, icon, temp, feels_like, humidity = ow.openweather()
    if(status_code == 200):
        owmainValue.set(main)

        # 取得 icon 圖片 bytes 資料
        raw_data = ow.openweatherIcon(icon)
        # 轉成 image 格式
        im = Image.open(BytesIO(raw_data))
        # 轉成 Tk 的 photo 格式
        photo = ImageTk.PhotoImage(im)
        # 配置到目標區(owiconLabel)
        owiconLabel.config(image=photo)
        owiconLabel.image=photo

        owtempValue.set("%.1f C" % (float(temp)-273.15))
        owfeelsLikeValue.set("%.1f C" % (float(feels_like)-273.15))
        owhumidityValue.set("%.1f %%" % float(humidity))

        sendData("A%.2f,%.2f" % ((float(temp)-273.15), float(humidity)))
    else:
        owmainValue.set('錯誤碼：' + str(status_code))

if __name__ == '__main__':

    try:
        ser = serial.Serial(COM_PORT, BAUD_RATES)
    except Exception as e:
        print("Serial exception: ", e)

    root = tkinter.Tk()
    root.geometry("800x400")
    root.title("Arduino 智慧家庭")

    myfont1 = font.Font(family='Helvetica', size=36, weight='bold')
    myfont2 = font.Font(family='Helvetica', size=24)

    buzeer_open_photo = ImageTk.PhotoImage(Image.open('buzeer_open.png'))
    buzeer_close_photo = ImageTk.PhotoImage(Image.open('buzeer_close.png'))
    clear_photo = ImageTk.PhotoImage(Image.open('clear.png'))
    red_photo = ImageTk.PhotoImage(Image.open('red.png'))
    green_photo = ImageTk.PhotoImage(Image.open('green.png'))
    yellow_photo = ImageTk.PhotoImage(Image.open('yellow.png'))
    door_open_photo = ImageTk.PhotoImage(Image.open('door_open.png'))
    door_close_photo = ImageTk.PhotoImage(Image.open('door_close.png'))

    # 爬蟲 Openweather -----------------------------------------------------------------
    owmainValue = tkinter.StringVar()
    owmainValue.set("")

    owtempValue = tkinter.StringVar()
    owtempValue.set("")

    owfeelsLikeValue = tkinter.StringVar()
    owfeelsLikeValue.set("")

    owhumidityValue = tkinter.StringVar()
    owhumidityValue.set("")
    # ----------------------------------------------------------------------------------
    cdsValue = tkinter.StringVar()
    cdsValue.set("0 lu")

    tempValue = tkinter.StringVar()
    tempValue.set("00.00 C")

    humiValue = tkinter.StringVar()
    humiValue.set("00.00%")

    respText = tkinter.StringVar()
    respText.set("0,0.0,0.0")

    sendButton0  = tkinter.Button(text='16', image=buzeer_close_photo, command=lambda: sendData('16'), font=myfont2)
    sendButton1  = tkinter.Button(text='1', image=red_photo, command=lambda: sendData('1'), font=myfont2)
    sendButton2  = tkinter.Button(text='2', image=green_photo, command=lambda: sendData('2'), font=myfont2)
    sendButton3  = tkinter.Button(text='3', image=yellow_photo, command=lambda: sendData('3'), font=myfont2)
    sendButton4  = tkinter.Button(text='4', image=door_close_photo, command=lambda: openTheDoor(), font=myfont2)
    # 爬蟲 Openweather -----------------------------------------------------------------
    owmainButton = tkinter.Button(textvariable=owmainValue, command=lambda: getOpenWeatherData(), font=myfont2)
    owiconLabel = tkinter.Label(root, image=None)
    owtempLabel = tkinter.Label(root, textvariable=owtempValue, font=myfont2, fg='#005100')
    owfeelsLikeLabel = tkinter.Label(root, textvariable=owfeelsLikeValue, font=myfont2, fg='#005100')
    owhumidityLabel = tkinter.Label(root, textvariable=owhumidityValue, font=myfont2, fg='#0000ff')
    # ----------------------------------------------------------------------------------
    cdsLabel = tkinter.Label(root, textvariable=cdsValue, font=myfont1, fg='#ff0000')
    tempLabel = tkinter.Label(root, textvariable=tempValue, font=myfont1, fg='#005100')
    humiLabel = tkinter.Label(root, textvariable=humiValue, font=myfont1, fg='#00f')
    receiveLabel = tkinter.Label(root, textvariable=respText)

    root.rowconfigure((0,1,2), weight=1) # 列 0, 列 1 同步放大縮小
    root.columnconfigure((0,1,2,3,4,5), weight=1) # 欄 0, 欄 1, 欄 2 ...同步放大縮小

    sendButton0.grid(row=0,   column=0, columnspan=1, sticky='EWNS')
    sendButton1.grid(row=0,   column=1, columnspan=1, sticky='EWNS')
    sendButton2.grid(row=0,   column=2, columnspan=1, sticky='EWNS')
    sendButton3.grid(row=0,   column=3, columnspan=1, sticky='EWNS')
    sendButton4.grid(row=0,   column=4, columnspan=2, sticky='EWNS')
    # 爬蟲 Openweather -----------------------------------------------------------------
    owiconLabel.grid(row=1, column=0, columnspan=1, sticky='EWNS')
    owmainButton.grid(row=1, column=1, columnspan=2, sticky='EWNS')
    owtempLabel.grid(row=1, column=3, columnspan=1, sticky='EWNS')
    owfeelsLikeLabel.grid(row=1, column=4, columnspan=1, sticky='EWNS')
    owhumidityLabel.grid(row=1, column=5, columnspan=1, sticky='EWNS')
    # ----------------------------------------------------------------------------------
    cdsLabel.grid(row=2,  column=0, columnspan=2, sticky='EWNS')
    tempLabel.grid(row=2, column=2, columnspan=2, sticky='EWNS')
    humiLabel.grid(row=2, column=4, columnspan=2, sticky='EWNS')
    # ----------------------------------------------------------------------------------
    receiveLabel.grid(row=3,  column=0, columnspan=6, sticky='EWNS')

    t1 = threading.Thread(target=receiveData)
    t1.start()

    t2 = threading.Thread(target=getOpenWeatherData)
    t2.start()

    root.mainloop()
