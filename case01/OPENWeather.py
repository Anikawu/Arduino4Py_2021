import requests
import urllib.request
import json
import ssl
# 不用驗證 SSL
ssl._create_default_https_context = ssl._create_unverified_context

def openweatherIcon(icon):
    img_url = 'https://openweathermap.org/img/wn/%s@2x.png' % icon
    raw_data = urllib.request.urlopen(img_url).read()
    return raw_data

def openweather():
    city = 'taoyuan'
    country = 'tw'
    apikey = '3b657e4dc92918d9d95fff4633377535'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'\
          .format(city, country, apikey)

    resp = requests.get(url)
    status_code = resp.status_code
    if(status_code == 200):
        jo = json.loads(resp.text)
        #print(jo)
        main = jo['weather'][0]['main']
        icon = jo['weather'][0]['icon']
        temp = jo['main']['temp']
        feels_like = jo['main']['feels_like']
        humidity = jo['main']['humidity']
        #print(main, icon, temp, feels_like, humidity)
        return status_code, main, icon, temp, feels_like, humidity
    else:
        print('Error', resp.status_code)
        return status_code, None, None, None, None, None

if __name__ == '__main__':
    status_code, main, icon, temp, feels_like, humidity = openweather()
    print(status_code, main, icon, temp, feels_like, humidity)
    print(openweatherIcon(icon))