import os
from collections import namedtuple

import requests

default_excludes = "daily,minutely,hourly,alerts"

LocationData = namedtuple("LocationData", ["lat", "lon"])


def extract_weather_data(coordinates: LocationData):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if os.getenv("USE_MOCK_API", "True").lower() == "true":
        api_url = "http://localhost:5050/data/3.0/onecall?"
    else:
        api_url = (
            f"https://api.openweathermap.org/data/3.0/onecall?appid={api_key}"
            f"&units=metric&exclude={default_excludes}&"
        )
    base_url = f"{api_url}lat={coordinates.lat}&lon={coordinates.lon}"
    response = requests.get(base_url)
    data = response.json()
    return data
