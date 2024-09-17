import os
from weather_etl_pipeline.extract import LocationData, extract_weather_data
from weather_etl_pipeline.load import load_data_to_db
from weather_etl_pipeline.read_coordinates import read_coordinates_from_postgres
from weather_etl_pipeline.transform import transform_weather_data_list

db_uri = os.getenv(
    "DATABASE_URL", "postgresql://weather_etl:weather_etl@localhost:5432/weather_db"
)


coordinates_df = read_coordinates_from_postgres(db_uri=db_uri)

weather_data_list = []

for _, coordinate in coordinates_df.iterrows():
    location_data = LocationData(coordinate["lat"], coordinate["lon"])
    raw_data = extract_weather_data(location_data)
    weather_data_list.append(raw_data)

clean_data_df = transform_weather_data_list(weather_data_list)
load_data_to_db(weather_data=clean_data_df, db_uri=db_uri)
