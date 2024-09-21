import json
from pathlib import Path

from flask import Flask, abort, jsonify, request

app = Flask(__name__)

# Define the path to the mock data folder
MOCK_DATA_FOLDER = Path("mock_data")


# Route to simulate OpenWeather API v3.0 OneCall
@app.route("/data/3.0/onecall", methods=["GET"])
def get_weather():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        abort(400, description="Missing 'lat' or 'lon' parameter")

    # Find the correct mock file based on lat/lon (e.g., London_weather.json)
    city = None
    for file in MOCK_DATA_FOLDER.glob("*_weather.json"):
        with open(file, "r") as f:
            weather_data = json.load(f)
            if str(weather_data["lat"]) == str(lat) and str(weather_data["lon"]) == str(
                lon
            ):
                city = file.stem
                break

    if not city:
        abort(
            404, description=f"Mock data for coordinates lat={lat}, lon={lon} not found"
        )

    # Return the corresponding mock data
    file_path = MOCK_DATA_FOLDER / f"{city}.json"
    with open(file_path, "r") as f:
        weather_data = json.load(f)

    return jsonify(weather_data)


if __name__ == "__main__":
    # Ensure the mock_data folder exists
    if not MOCK_DATA_FOLDER.exists():
        print(f"Mock data folder '{MOCK_DATA_FOLDER}' not found.")
        exit(1)

    app.run(host="0.0.0.0", debug=True, port=5050)
