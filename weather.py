#coding:utf-8
import json
import requests

params = {"version":"1", "city":"부산", "county":"영도구", "village":"동삼동"}
headers = {"appKey":"0ee18f4c-d394-3b83-aab4-3bdc6e2a90a5"}

r = requests.get("http://apis.skplanetx.com/weather/current/hourly", params=params, headers=headers)

#print (r.json())

data = json.loads(r.text)

weather = data["weather"]["hourly"]
cGrid = weather[0]["grid"]
cLoc = cGrid["city"] + " " + cGrid["county"] + " " + cGrid["village"]
cTime = weather[0]["timeRelease"]
#cTime2 = cTime.strftime('%Y년 %m월 %d일  %H시 %M분')
cSky = weather[0]["sky"]["name"]
cWind = weather[0]["wind"]["wspd"]
cTemp = weather[0]["temperature"]["tc"]
cHum = weather[0]["humidity"]

cWeather = cLoc + "의 날씨(" + cTime + " 기준): " + cSky + ", 풍속은 " + cWind, "m/s, 기온은 {0:0.1f}도, 습도는 {1:0.1f}% 입니다.".format(cTemp, cHum)

print (cWeather)

