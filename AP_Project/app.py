from flask import Flask, render_template, request
from datetime import datetime as dt
import requests
import turtle as trtl
import time as tm
from pprint import pprint
import flickrapi
import json

apikey = '5f709e8887d22a3d3dd21ed7c27d5989'
apisecret = '52d44856e72655cf'


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "e7830c51a2f03f19bbecd951b282df16"

account_email='arjun.rasane@gmail.com'

def kel_cel_fer(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit

#initialize
flickr = flickrapi.FlickrAPI(apikey, apisecret, format='parsed-json')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    CITY = request.form['city']
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    x = (response['cod'])
    if x == 200:
        temp_kelvin = response['main']['temp']
        temp_cel, temp_fer = kel_cel_fer(temp_kelvin)
        time_difference = response['timezone']
        local_time = tm.time()
        local_time = local_time + 25200
        local_time = local_time + time_difference
        local_time = round(local_time)
        local_time = dt.fromtimestamp(local_time)

        temp_fer = round(int(temp_fer))
        weathersList = response['weather']
        for weather in weathersList:
            condition = (weather['description'])

        city_name =  CITY + " architecture"

        photos = flickr.photos.search(text = city_name,extras="url_c" ,per_page='10')

        json_object = json.dumps(photos, indent = 0) 
        parsed_data = json.loads(json_object)
        if parsed_data['photos']['total'] == 0:
            url_c = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
        else:
            url_c = parsed_data['photos']['photo'][0]['url_c']
        white = "white_img.png"
        return render_template('index.html', city=CITY, image_url=url_c, temp_fer = temp_fer, local_time = local_time, condition = condition, white = white)
    else:
        err = "City not valid"
        return render_template('index.html',err_text=err)

if __name__ == '__main__':
    app.run(debug=True)


