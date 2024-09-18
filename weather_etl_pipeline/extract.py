import os
from collections import namedtuple

import requests

default_excludes = "daily,minutely,hourly,alerts"

LocationData = namedtuple("LocationData", ["lat", "lon"])


def extract_weather_data(coordinates: LocationData):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    base_url = (
        f"https://api.openweathermap.org/data/3.0/onecall?"
        f"lat={coordinates.lat}&lon={coordinates.lon}"
        f"&exclude={default_excludes}&units=metric&appid={api_key}"
    )
    response = requests.get(base_url)
    data = response.json()
    return data
