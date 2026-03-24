<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&pause=1000&color=3B82F6&center=true&vCenter=true&width=600&lines=Uber+Trip+Analytics+Pipeline" alt="Typing SVG" />

### End-to-end cloud data pipeline — ingestion, transformation, warehousing & orchestration

![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20RDS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-4.1-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-1.11-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-3.0-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-RDS-336791?style=for-the-badge&logo=postgresql&logoColor=white)

</div>

---

## What This Project Does

This pipeline ingests raw Uber-style trip data, validates and transforms it through a medallion architecture, loads it into a cloud data warehouse, and surfaces business-ready analytics — all orchestrated automatically on a daily schedule with retry logic and quality gates.

---

## Key Metrics

| Metric | Value |
|--------|-------|
| Daily records processed | **10,000+** |
| dbt models | **7** |
| Data quality tests | **12 — 100% pass rate** |
| Airflow DAG tasks | **8** |
| Top revenue zone | **Airport — $49,721** |
| Peak hour | **Midnight — 467 trips** |

---

## Pipeline DAG
```
generate_data → quality_checks → upload_s3 → silver_transform → gold_transform → load_postgres → dbt_run → dbt_test
```
> Each task has retry logic — no downstream task runs if an upstream check fails.

---

## Medallion Architecture

| Layer | Storage | Description |
|-------|---------|-------------|
| **Bronze** | AWS S3 | Raw CSV files, partitioned by date |
| **Silver** | AWS S3 | Cleaned Parquet — deduped, typed, validated |
| **Gold** | PostgreSQL RDS | Business aggregations — zone revenue, driver KPIs |

---

## Tech Stack

| Category | Tool |
|----------|------|
| Cloud Storage | AWS S3 |
| Data Processing | PySpark |
| Data Warehouse | AWS RDS (PostgreSQL) |
| Data Modeling | dbt |
| Orchestration | Apache Airflow |
| Language | Python 3.11, SQL |

---

## Business Insights Generated

- **Zone Revenue Analysis** — Airport tops at $49,721 across all pickup zones
- **Driver Performance Metrics** — trip counts, avg fare, completion rates
- **Surge Pricing Patterns** — peak demand at midnight with 467 trips
- **Trip Trend Monitoring** — daily/weekly volume tracking dashboard

---

## Project Structure
```
uber-trip-pipeline/
├── airflow/            # DAG definitions and task configs
├── ingestion/          # Data generation and S3 upload scripts
├── transformations/    # PySpark Bronze → Silver → Gold logic
├── dbt_project/        # dbt models, tests, schema definitions
├── dashboards/         # Streamlit analytics dashboard
├── docs/               # Architecture diagrams
└── logs/               # Pipeline execution logs
```

---

## How to Run
```bash
pip install -r requirements.txt
python ingestion/generate_data.py
airflow dags trigger uber_trip_pipeline
cd dbt_project && dbt run && dbt test
```

---

## Resume Bullets

- Built end-to-end Trip Analytics Pipeline using Python, PySpark, AWS S3, PostgreSQL RDS, dbt, and Airflow
- Designed medallion architecture (Bronze/Silver/Gold) processing 10,000+ daily trip records
- Implemented 7 dbt models with 12 automated data quality tests achieving 100% pass rate
- Orchestrated daily pipeline with 8-task Airflow DAG including retry logic and quality gates
- Surfaced business insights across zone revenue, driver performance, and surge pricing trends
