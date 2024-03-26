import datetime as dt
import requests
import turtle as trtl
import time
 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "e7830c51a2f03f19bbecd951b282df16"


CITY = input("Pick a city: ")




def kel_cel_fer(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()



temp_kelvin = response['main']['temp']
temp_cel, temp_fer = kel_cel_fer(temp_kelvin)

#work on time later(it isnt working)
''''
time_difference = response['timezone']
print(time_difference)


if time_difference <= 0:

    time = time.time()
    time = int(time + 25200 - 50400)
    time = int(time - time_difference)
    time = int(round(time * 1000))
else:
    time = time.time()
    time = int(time + 25200 + 50400)
    time = int(time - time_difference)
    time = int(round(time * 1000))

print(time)
'''
date = dt.time()
temp_fer = round(int(temp_fer))
print(temp_fer)
wn = trtl.Screen()
UI = trtl.Turtle()



UI.penup()
UI.goto(-350,350)
UI.write(CITY, font = ("Times", "24", "bold italic"))
UI.right(90)
UI.forward(40)
UI.left(90)

deg_sym = "°"

UI.write("the tempreture is: ", temp_fer, font = ("Times", "24", "bold italic"))
UI.write( temp_fer, "°", font = ("Times", "24", "bold italic"))
UI.write(deg_sym, font = ("Times", "24", "bold italic"))

UI.goto(-350,350)
UI.right(90)
UI.forward(80)
UI.left(90)
UI.write(date, font = ("Times", "24", "bold italic"))

wn.mainloop()
