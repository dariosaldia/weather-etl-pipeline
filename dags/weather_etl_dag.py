import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 9, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "weather_etl_dag",
    default_args=default_args,
    description="Run weather ETL using Docker",
    schedule_interval=timedelta(hours=1),  # Adjust the schedule as needed
    catchup=False,
) as dag:

    openweather_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    db_url = os.getenv("DATABASE_URL")
    docker_image = os.getenv("WEATHER_ETL_IMAGE")

    # Define the DockerOperator
    run_etl = DockerOperator(
        task_id="run_weather_etl",
        image=docker_image,
        container_name="weather_etl_container",
        auto_remove=True,  # Automatically remove container after it finishes
        docker_url="unix://var/run/docker.sock",  # Docker socket to run the container
        network_mode="weather_etl_network",  # Specify network mode if needed
        mount_tmp_dir=False,  # Avoids mounting temporary directories
        tty=True,  # Enable terminal output in the logs
        environment={
            "OPENWEATHERMAP_API_KEY": openweather_api_key,
            "DATABASE_URL": db_url,
        },
    )
