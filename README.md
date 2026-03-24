# 🚗 Uber Trip Analytics Data Pipeline

![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20RDS-orange)
![PySpark](https://img.shields.io/badge/PySpark-4.1-red)
![dbt](https://img.shields.io/badge/dbt-1.11-orange)
![Airflow](https://img.shields.io/badge/Airflow-3.0-blue)
![Python](https://img.shields.io/badge/Python-3.11-blue)

## Project Overview
End-to-end cloud data pipeline for Uber/DoorDash-style trip analytics.

## Tech Stack
- Cloud Storage: AWS S3
- Transformation: PySpark
- Warehouse: AWS RDS PostgreSQL
- Modeling: dbt (7 models, 12 tests)
- Orchestration: Apache Airflow
- Language: Python 3.11, SQL

## Medallion Architecture
- Bronze: Raw CSV files in S3 (partitioned by date)
- Silver: Cleaned Parquet files (deduped, typed, validated)
- Gold: Business aggregations (zone revenue, driver performance)

## Key Metrics
- 10,000 daily trip records processed
- 7 dbt models with 12 data quality tests
- 8-task Airflow DAG running daily
- Top Revenue Zone: Airport ($49,721)
- Peak Hour: Midnight (467 trips)

## Pipeline DAG
generate_data > quality_checks > upload_s3 > silver_transform > gold_transform > load_postgres > dbt_run > dbt_test

## Resume Bullet Points
- Built end-to-end Trip Analytics Pipeline using Python, PySpark, AWS S3, PostgreSQL RDS, dbt, and Airflow
- Designed medallion architecture (Bronze/Silver/Gold) processing 10,000+ daily trip records
- Implemented 7 dbt models with 12 automated data quality tests (100% pass rate)
- Orchestrated daily pipeline with 8-task Airflow DAG with retry logic and quality gates
- Generated business insights: zone revenue, driver performance, surge pricing analysis
