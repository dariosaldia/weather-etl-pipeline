CREATE ROLE airflow LOGIN PASSWORD 'airflow';
CREATE DATABASE airflow;
\c airflow postgres;
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
GRANT USAGE ON SCHEMA public TO airflow;
GRANT CREATE ON SCHEMA public TO airflow;

CREATE ROLE weather_etl LOGIN PASSWORD 'weather_etl';

\c postgres;
GRANT pg_read_server_files TO weather_etl;

CREATE DATABASE weather_db;
\c weather_db postgres;
GRANT ALL PRIVILEGES ON DATABASE weather_db TO weather_etl;
GRANT USAGE ON SCHEMA public TO weather_etl;
GRANT CREATE ON SCHEMA public TO weather_etl;

\c weather_db weather_etl;

CREATE TABLE "cities_data" (
  "id" smallserial,
  "city" character varying NOT NULL,
  "lon" numeric NOT NULL,
  "lat" numeric NOT NULL
);

COPY "cities_data" (city, lat, lon)
FROM '/docker-entrypoint-initdb.d/worldcities.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE "weather_data" (
  "lon" numeric NOT NULL,
  "lat" numeric NOT NULL,
  "temperature" numeric NOT NULL,
  "humidity" numeric NOT NULL,
  "wind_speed" numeric NOT NULL,
  "description" character varying NOT NULL,
  "date" timestamp NOT NULL
);
