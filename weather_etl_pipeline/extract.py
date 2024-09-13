from collections import namedtuple
import os
import requests

default_excludes = "daily,minutely,hourly,alerts"

LocationData = namedtuple('LocationData', ['lat', 'lon'])

def extract_weather_data(coordinates: LocationData):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    base_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={coordinates.lat}&lon={coordinates.lon}&exclude={default_excludes}&units=metric&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    return data
