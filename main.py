
from datetime import datetime as dt
import requests
import turtle as trtl
import time


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "e7830c51a2f03f19bbecd951b282df16"

wn = trtl.Screen()
UI = trtl.Turtle()
UI.penup()
''''
UI.goto(-200, 0)
UI.write("Pick A City: ", font =  ("times","24", "bold italic"))
UI.goto(-70,0)

wn.listen()

wn.onkeypress("a")
'''


CITY = input("Pick a city: ")




def kel_cel_fer(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
x = (response['cod'])


while x != 200: 
    response['message']
    print("city not valid")
    CITY = input("Pick a city: ")
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    x = (response['cod'])
        

else:



    temp_kelvin = response['main']['temp']
    temp_cel, temp_fer = kel_cel_fer(temp_kelvin)

#work on time later(it isnt working)

    time_difference = response['timezone']

    time = time.time()
    time = time + 25200
    time = time + time_difference
    time = round(time)



    time = dt.fromtimestamp(time)


    print(time)



    temp_fer = round(int(temp_fer))
    print(temp_fer)




    UI.penup()
    UI.goto(-730, 370)
    UI.write(CITY, font = ("Herculanum", "75", "bold italic"))
    UI.right(90)
    UI.forward(80)
    UI.left(90)
    deg_sym = "°F"
    UI.write( temp_fer, "°", font = ("Herculanum", "60", "bold italic"))
    UI.write(deg_sym, font = ("Herculanum", "60", "bold italic"))

    UI.goto(-730,370)
    UI.right(90)
    UI.forward(120)
    UI.left(90)
    UI.write(time, font = ("Herculanum", "24", "bold italic"))


    wn.mainloop()

