<div align="center">


  <img src="https://img.shields.io/badge/DATA_ENGINEERING-UBER_PIPELINE-0071e3?style=for-the-badge&logo=uber&logoColor=white" />


  <h1>🚀 Uber Trip Analytics Pipeline</h1>


  <p><b>An enterprise-grade, end-to-end data lakehouse pipeline orchestrating raw trip data into business-ready analytics.</b></p>


<a href="https://subhiksharavichandran.github.io/uber-trip-pipeline/"><b>➔ View Live Interactive Dashboard & Case Study</b></a>

<br/><br/>

GIF_PLACEHOLDER

</div>


<br>


<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=Apache-Airflow&logoColor=white" />
  <img src="https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Amazon_S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white" />
</div>


<br>


💡 Executive Summary
This robust architecture processes 10,000+ daily Uber trip records. It systematically takes raw, disjointed logs and refines them through a rigid Medallion Architecture (Bronze ➔ Silver ➔ Gold). Orchestrated entirely by Apache Airflow and validated via dbt, the pipeline guarantees zero-defect data routing into a PostgreSQL warehouse for downstream BI analytics.
⸻
🎛️ Interactive Architecture Deep-Dive

(Click on a layer to expand and see what happens inside!)

<details>
<summary><b>1️⃣ 🥉 The Bronze Layer (Raw Ingestion)</b></summary>
<br>
<blockquote>
Incoming raw Uber CSV datasets are ingested without modification into an AWS S3 Data Lake. This ensures we always have an immutable historical audit trail of the exact data as it arrived.
</blockquote>
</details>


<details>
<summary><b>2️⃣ 🥈 The Silver Layer (Standardization)</b></summary>
<br>
<blockquote>
Using <b>Pandas & PySpark</b>, the pipeline drops completely null rows, standardizes timestamp formats (e.g. <code>tpep_pickup_datetime</code>), and casts monetary fields to strict float profiles. The data is now clean, validated, and staged for business aggregation.
</blockquote>
</details>


<details>
<summary><b>3️⃣ 🥇 The Gold Layer (Business Logic & Analytics)</b></summary>
<br>
<blockquote>
The final tier aggregates the granular data into wide, dimensional Star-Schema models (e.g. <code>fact_trips</code>, <code>dim_datetime</code>, <code>dim_location</code>). This data is highly optimized for low-latency BI queries and dashboarding.
</blockquote>
</details>

⸻
⏱️ Airflow DAG (Workflow Orchestration)

The entire pipeline is fully automated and runs without human intervention. The DAG executes the following structured workflow:

1. generate_data: Polls/Receives the newest daily trip logs.
2. quality_checks: Asserts basic row-count and formatting bounds.
3. upload_s3: Migrates the raw data to the cloud Bronze bucket.
4. silver_transform: Executes the Python/Spark cleaning scripts.
5. gold_transform: Runs aggregation calculations.
6. load_postgres: Upserts the final metrics into the Data Warehouse.
7. dbt_run & dbt_test: Executes 7 SQL models and 12 referential integrity tests to guarantee data SLA standards.
⸻
📂 Repository Structure

uber-trip-pipeline/
│
├── 📁 data/
│   ├── raw/                 # Local staging for raw CSVs
│   └── processed/           # Cleaned flat-files before warehouse load
│
├── 📁 dags/                 # Apache Airflow orchestration logic
│   └── uber_pipeline.py     # The main 8-task DAG
│
├── 📁 dbt/                  # Data Build Tool models
│   ├── models/              # fact and dimension SQL models
│   └── schema.yml           # referential integrity tests
│
├── 📄 bronze_to_silver.py   # Cleaning and PySpark transformations
├── 📄 silver_to_gold.py     # Aggregation algorithms
├── 📄 dashboard.py          # Dashboarding/BI serving code
├── 📄 index.html            # Interactive Portfolio Web Application
└── 📄 README.md             # Project Documentation

⸻
👨‍💻 Built By
Subhiksha Ravichandran

Data Engineer | GitHub Profile
