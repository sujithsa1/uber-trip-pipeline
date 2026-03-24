from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import subprocess
import sys

default_args = {
    "owner": "sujith",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

def generate_data():
    result = subprocess.run(
        [sys.executable, "/Users/sujithsuji/uber-trip-pipeline/ingestion/generate_data.py"],
        capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        raise Exception(result.stderr)

def run_quality_checks():
    import pandas as pd
    df = pd.read_csv("/Users/sujithsuji/uber-trip-pipeline/data/raw/trips.csv")
    assert df["trip_id"].isnull().sum() == 0
    assert (df["fare_amount"] < 0).sum() == 0
    assert df["trip_status"].isin(["completed","cancelled"]).all()
    print(f"✅ Quality checks passed! ({len(df)} rows)")

def upload_to_s3():
    result = subprocess.run(
        [sys.executable, "/Users/sujithsuji/uber-trip-pipeline/ingestion/upload_to_s3.py"],
        capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        raise Exception(result.stderr)

def run_silver():
    result = subprocess.run(
        [sys.executable, "/Users/sujithsuji/uber-trip-pipeline/transformations/bronze_to_silver.py"],
        capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        raise Exception(result.stderr)

def run_gold():
    result = subprocess.run(
        [sys.executable, "/Users/sujithsuji/uber-trip-pipeline/transformations/silver_to_gold.py"],
        capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        raise Exception(result.stderr)

def load_postgres():
    result = subprocess.run(
        [sys.executable, "/Users/sujithsuji/uber-trip-pipeline/ingestion/load_to_postgres.py"],
        capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        raise Exception(result.stderr)

with DAG(
    dag_id="uber_trip_pipeline",
    default_args=default_args,
    description="Uber Trip Analytics Pipeline",
    schedule="@daily",
    start_date=datetime(2026, 3, 1),
    catchup=False,
    tags=["uber", "trips", "analytics"]
) as dag:

    t1 = PythonOperator(task_id="generate_trip_data", python_callable=generate_data)
    t2 = PythonOperator(task_id="quality_checks", python_callable=run_quality_checks)
    t3 = PythonOperator(task_id="upload_s3_bronze", python_callable=upload_to_s3)
    t4 = PythonOperator(task_id="silver_transform", python_callable=run_silver)
    t5 = PythonOperator(task_id="gold_transform", python_callable=run_gold)
    t6 = PythonOperator(task_id="load_postgres", python_callable=load_postgres)
    t7 = BashOperator(
        task_id="dbt_run",
        bash_command="cd /Users/sujithsuji/uber-trip-pipeline/dbt_project && /Users/sujithsuji/uber-trip-pipeline/venv311/bin/dbt run"
    )
    t8 = BashOperator(
        task_id="dbt_test",
        bash_command="cd /Users/sujithsuji/uber-trip-pipeline/dbt_project && /Users/sujithsuji/uber-trip-pipeline/venv311/bin/dbt test"
    )

    t1 >> t2 >> t3 >> t4 >> t5 >> t6 >> t7 >> t8
