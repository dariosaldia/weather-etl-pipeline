import csv
import json
import os
from pathlib import Path

import requests

default_excludes = "daily,minutely,hourly,alerts"


# Function to fetch weather data from OpenWeather API v3.0 OneCall
def fetch_weather_data(lat, lon, api_key, city_name, output_folder):
    api_url = (
        f"https://api.openweathermap.org/data/3.0/onecall?"
        f"lat={lat}&lon={lon}"
        f"&exclude={default_excludes}&units=metric&appid={api_key}"
    )

    response = requests.get(api_url)

    if response.status_code == 200:
        weather_data = response.json()
        # Save response as JSON file
        output_path = Path(output_folder) / f"{city_name}_weather.json"
        with open(output_path, "w") as f:
            json.dump(weather_data, f, indent=4)
        print(f"Weather data for {city_name} saved to {output_path}")
    else:
        print(f"Failed to fetch weather data for {city_name}: {response.status_code}")


if __name__ == "__main__":
    # Ensure the API_KEY environment variable is set
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        print("Please set the OPENWEATHERMAP_API_KEY environment variable.")
        exit(1)

    # Path to the CSV file with city coordinates
    csv_file = "scripts/init/sql/worldcities.csv"

    # Create a folder to store the mock data if it doesn't exist
    output_folder = "mock_data"
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Open and read the CSV file
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row["city"]
            lat = row["lat"]
            lon = row["lon"]
            print(f"Fetching weather data for {city} (lat: {lat}, lon: {lon})")
            fetch_weather_data(lat, lon, api_key, city, output_folder)
