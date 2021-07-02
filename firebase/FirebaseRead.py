import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://arduino-iot-2021-default-rtdb.firebaseio.com/'

})
door=db.reference('/door').get()
print(door)
temp=db.reference('/dht11/temp').get()
humi=db.reference('/dht11/humi').get()
print(temp,humi)
dht11=db.reference('/dht11').get()
print(dht11,dht11['temp'],dht11['humi'])

def listener(event):
    print(event.data)
#listener
firebase_admin.db.reference("/door").listen(listener)