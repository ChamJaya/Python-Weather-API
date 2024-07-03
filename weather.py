import json
# import requests
import os

from dotenv import load_dotenv

load_dotenv()

def get_current_weather(city="Colombo, LKR"):
    requeste_url = f'111111'
    # requeste_url = f'https://api.openweathermap.org/data/2.5/weather?id=524901&appid=f4706c861a6801db0d8f17354f357cb2&q=Colombo,%20LK&units=metric'

    # weather_data = requests.get(requeste_url).json()
    weather_data = fake_weather_info()

    return weather_data

def fake_weather_info():
    """Fixture that returns a static weather data."""
    with open("weather.json") as f:
        return json.load(f)

if __name__ == "__main__":
    print('/n*** get Current Weather Conditions ***/n')

    city = input("/n Please enter a city name: ")

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city="Colombo"
        

    weather_data = get_current_weather(city)

    print("/n")
    print(weather_data)

