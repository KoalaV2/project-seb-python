#!/usr/bin/env python3
import requests, json 
from library.utils import say
import speech_recognition as sr 

r = sr.Recognizer()
def weather():
    with sr.Microphone() as source:
        api_key = "886705b4c1182eb1c69f28eb8c520e20"

        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        say("What is the city name?")
        print("What is the city name?")
        city_name_listen = r.listen(source)
        city_name = r.recognize_google(city_name_listen) 

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

        response = requests.get(complete_url) 
        
        x = response.json() 

        if x["cod"] != "404": 
        

            y = x["main"] 
        

            current_temperature = y["temp"] 
        
            #current_pressure = y["pressure"] 
        
            #current_humidiy = y["humidity"] 
        
            z = x["weather"] 
        

            weather_description = z[0]["description"] 
            print("It is " + str(current_temperature) + " Celsius in " + city_name + " with " + str(weather_description)) 
            say("It is " + str(current_temperature) + " Celsius in " + city_name + " with " + str(weather_description))

        else: 
            print(" City Not Found ")
