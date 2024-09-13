from typing import Dict, List
import pandas as pd

def transform_weather_data_list(weather_data: List) -> List:
    return list(map(lambda data: transform_weather_data_object(data), weather_data))

def transform_weather_data_object(data: Dict) -> Dict:
    return {
        'lon': data['lon'],
        'lat': data['lat'],
        'temperature': data['current']['temp'],
        'humidity': data['current']['humidity'],
        'wind_speed': data['current']['wind_speed'],
        'description': data['current']['weather'][0]['description'],
        'date': pd.Timestamp.now()
    }
