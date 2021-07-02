import tkinter
from tkinter import font
import threading
from PIL import Image, ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://arduino-iot-2021-default-rtdb.firebaseio.com/'

})
def listenerDoor(event):
    print(event.data)

    if event.data== 1:  #開門
        doorLabel.config(image=door_open_photo)
        doorLabel.image = door_open_photo
    elif event.data== 0:
        doorLabel.config(image=door_close_photo)
        doorLabel.image = door_close_photo


def listenerDHT11Temp(event):
    print(event.data)
    tempValue.set(event.data)

def listenerDHT11Humi(event):
    print(event.data)
    humiValue.set(event.data)

def listenerFirebase():
    firebase_admin.db.reference("/door").listen(listenerDoor)
    firebase_admin.db.reference("/dht11/temp").listen(listenerDHT11Temp)
    firebase_admin.db.reference("/dht11/humi").listen(listenerDHT11Humi)

root = tkinter.Tk()
root.geometry("500x150")
root.title("Firebase console")

myfont = font.Font(family='Helvetica', size=36, weight='bold')

door_open_photo  = ImageTk.PhotoImage(Image.open('door_open.png'))
door_close_photo = ImageTk.PhotoImage(Image.open('door_close.png'))

tempValue = tkinter.StringVar()
tempValue.set("00.0 C")

humiValue = tkinter.StringVar()
humiValue.set("00.0 %")

tempLabel = tkinter.Label(root, textvariable=tempValue, font=myfont)
humiLabel = tkinter.Label(root, textvariable=humiValue, font=myfont)
doorLabel = tkinter.Label(root, image=door_close_photo, font=myfont)

root.rowconfigure(0, weight=1)
root.columnconfigure((0, 1, 2), weight=1)

tempLabel.grid(row=0, column=0, sticky='EWNS')
humiLabel.grid(row=0, column=1, sticky='EWNS')
doorLabel.grid(row=0, column=2, sticky='EWNS')

t1 = threading.Thread(target=listenerFirebase)
t1.start()

root.mainloop()