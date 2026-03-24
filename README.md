<div align="center">
  <img alt="Uber Pipeline" src="https://img.shields.io/badge/Uber%20Data%20Pipeline-000000?style=for-the-badge&logo=uber&logoColor=white" />
  <br/>
  <h1>Data Infrastructure & Orchestration</h1>
  <p><b>An enterprise-grade, highly-available, end-to-end data lakehouse pipeline for ride-share telemetry.</b></p>
  <br/>


Interactive Dashboard 
  
Python 3.9+ 
Status
</div>


<br/>


🏗️ System Architecture

This project processes over 10,000+ daily ride-share telemetry logs, taking raw disjointed CSVs and refining them through a strict Medallion Architecture. The entire directed acyclic graph (DAG) is orchestrated by Apache Airflow.

graph TD
    subgraph Data Lake [AWS S3 Cloud Storage]
        A[(Raw Bronze)] -->|"Clean & Standardize \n (Pandas)"| B[(Validated Silver)]
    end

    subgraph Data Warehouse [PostgreSQL Server]
        B -->|"Aggregate \n (PySpark)"| C[(Business Gold)]
        C -->|"Schema Integrity \n (dbt)"| D[(Analyzed Fact/Dim)]
    end

    subgraph BI Layer [Serving]
        D -->|SQL Queries| E[Executive Dashboard]
    end

    style Data Lake fill:#fbfbfd,stroke:#d2d2d7,stroke-width:2px;
    style Data Warehouse fill:#ffffff,stroke:#0071e3,stroke-width:2px;
    style BI Layer fill:#f5f5f7,stroke:#86868b,stroke-width:2px;
    
    style A fill:#a66f44,color:#fff;
    style B fill:#86868b,color:#fff;
    style C fill:#f59e0b,color:#000;

⸻
⚙️ Engineering Specs

1. The Airflow DAG (uber_pipeline.py)
The pipeline runs without human intervention via an 8-task dependency chain:
1. generate_remote_data: Ingests latest upstream CSVs.
2. quality_checks: Asserts payload structure.
3. upload_s3: Migrates to Bronze bucket.
4. silver_transform: Handles null-filtering and timestamp normalization.
5. gold_transform: Calculates zone-based revenue dimensions.
6. load_postgres: Upserts into the relational database.
7. dbt_run & dbt_test: Freezes execution if referential tests fail.

2. Data Build Tool (dbt)
The warehouse relies on strictly-typed data models:
- 7 SQL Models: Segmenting fact_trips, dim_temporal, and dim_spatial_zones.
- 12 SLA Tests: Automatically declining data if anomalies (like negative trip fares or impossible coordinate bounds) are detected.
⸻
🚀 Quickstart / Local Execution

To spin up the infrastructure on your local machine:

# 1. Clone the repository
git clone https://github.com/SubhikshaRavichandran/uber-trip-pipeline.git
cd uber-trip-pipeline

# 2. Deploy the local Airflow environment
make airflow-up

# 3. Mount PostgreSQL DB
docker-compose up -d postgres

# 4. Trigger the initial pipeline run
airflow dags trigger uber_trip_ingestion_v1

⸻
📂 Repository Topology

uber-trip-pipeline/
├── data/                    # Local staging (ignored in production)
├── dags/                    # Apache Airflow definitions
│   └── uber_pipeline.py     # Core 8-task orchestration logic
├── dbt/                     # Data Build Tool configurations
│   ├── models/              # fact and dimension architectures
│   └── schema.yml           # referential integrity validations
├── scripts/
│   ├── bronze_to_silver.py  # Cleaning and PySpark mappings
│   ├── silver_to_gold.py    # Aggregation algorithms
│   └── dashboard.py         # App serving code
└── index.html               # Presentation Website

⸻
Engineered natively by Subhiksha Ravichandran
