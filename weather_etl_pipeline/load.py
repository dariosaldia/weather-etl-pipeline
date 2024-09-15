import pandas as pd
from typing import List
from sqlalchemy import create_engine

def load_data_to_db(weather_data: List, db_uri: str):
    df = pd.DataFrame(weather_data)
    engine = create_engine(db_uri)
    df.to_sql('weather_data', engine, if_exists='replace', index=False)
