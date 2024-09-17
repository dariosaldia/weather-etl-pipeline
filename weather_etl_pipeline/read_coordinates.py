import pandas as pd
from sqlalchemy import create_engine

def read_coordinates_from_postgres(db_uri: str) -> pd.DataFrame:
    """
    Fetch data from a PostgreSQL database and load it into a pandas DataFrame using SQLAlchemy.
    
    Parameters:
    - query: The SQL query string to execute.
    
    Returns:
    - A pandas DataFrame containing the query results.
    """
    try:
        # Create an SQLAlchemy engine
        engine = create_engine(db_uri)
        
        query = "SELECT * FROM cities_data"
        
        # Read the SQL query into a pandas DataFrame
        df = pd.read_sql_query(query, engine)
        
        return df
    except Exception as e:
        print(f"Error: {e}")
