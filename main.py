import requests
import json
import sqlite3
import time

#air pollution openweathermap.
key = "74110bbef509e33cd1e0997402276979"
getter = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={41.716667}&lon={44.783333}&appid={key}')
# print(getter.status_code, getter.text, getter.url, sep="\n")
getterJSON = getter.json()
# #მონაცემების შენახვა
with open("pollution.json" , "w") as weather:
    json.dump(getterJSON, weather, indent=4)

#ქალაქის კოორდინატები და კომპონენტები მხოლოდ პირველი ელემენტის
# coordinates = getterJSON['coord']
# print(coordinates)
# components = getterJSON['list'][0]['components']
# print(components)

conn = sqlite3.connect("weather.sqlite")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS pollutionInTbilisi
                  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  Longitude float,
                  latitude float,
                  Date varchar(15),
                  co float,
                  no float,
                  no2 float,
                  so2 float
                  );""")

#ფუნქციას unix დეითის სახის მონაცემი რომელიც json ფაილშია სახელით "dt"  გადაყავს MM/DD/YY HOUR ფორმატში
def unixToDate(var):
    return time.strftime("%D %H:%M", time.localtime(int(var)))

main = [i for i in getterJSON]
lst = []
for i in main:
    longitude = getterJSON[main[0]]['lon']
    latitude = getterJSON[main[0]]['lat']
    for j in getterJSON[main[1]][0:-1]:
        date =j['dt']
        co = j['components']['co']
        no = j['components']['no']
        no2 = j['components']['no2']
        so2 = j['components']['so2']
        var = (longitude, latitude, unixToDate(date), co, no, no2, so2)
        lst.append(var)

#ბაზაში შევიტანე ქალაქის longitude & latitude, თარიღი და დრო საათების მიხედვით და 4 სახის ნივთიერების მაჩვენებლები
cursor.executemany("INSERT INTO pollutionInTbilisi (Longitude, latitude, Date, co, no, no2, so2) values (?, ?, ?, ?, ?, ?, ?)", lst)
conn.commit()
conn.close()