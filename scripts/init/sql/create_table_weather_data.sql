

CREATE TABLE "weather_data" (
  "lon" numeric NOT NULL,
  "lat" numeric NOT NULL,
  "temperature" numeric NOT NULL,
  "humidity" numeric NOT NULL,
  "wind_speed" numeric NOT NULL,
  "description" character varying NOT NULL,
  "date" timestamp NOT NULL
);
