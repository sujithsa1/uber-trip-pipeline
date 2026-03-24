<div align="center">
  <img alt="Uber Pipeline" src="https://img.shields.io/badge/Uber%20Data%20Pipeline-000000?style=for-the-badge&logo=uber&logoColor=white" />
  <br/>
  <h1>Data Infrastructure & Orchestration</h1>
  <p><b>An enterprise-grade, highly-available, end-to-end data lakehouse pipeline for ride-share telemetry.</b></p>
  <br/>

# 🚗 Uber Trip Analytics Pipeline  

<div align="center">

![Pipeline](https://img.shields.io/badge/Data%20Pipeline-End--to--End-orange?style=for-the-badge)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-blue?style=for-the-badge&logo=apacheairflow)
![dbt](https://img.shields.io/badge/dbt-Transformation-orange?style=for-the-badge)
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20RDS-yellow?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)

### **End-to-End Data Pipeline transforming raw trip data into business insights**

🔗 **Live Portfolio:** https://subhi.github.io/uber-trip-pipeline/  
🔗 **GitHub Repo:** https://github.com/SubhikshaRavichandran/uber-trip-pipeline  

</div>

---

## ✨ Project Overview

This project is a complete data engineering pipeline that processes Uber-style trip data from raw CSV files to final analytics dashboards.

It simulates a real-world workflow where:
- Raw data is ingested  
- Cleaned and validated  
- Transformed into business metrics  
- Stored and served for analytics  

👉 The goal is to convert messy trip data into meaningful insights like:
- Revenue trends  
- Driver performance  
- Demand patterns  
- Surge pricing analysis  

---

## 🧠 Pipeline Flow


Raw Data (CSV)
↓
Bronze (S3 - Raw Storage)
↓
Silver (Cleaned & Validated Data)
↓
Gold (Business Aggregations)
↓
PostgreSQL (Serving Layer)
↓
Dashboard (Analytics)


---

## ⚙️ Airflow DAG


generate_data
→ quality_checks
→ upload_s3
→ silver_transform
→ gold_transform
→ load_postgres
→ dbt_run
→ dbt_test


✔ Fully automated  
✔ Runs daily  
✔ Includes data quality validation  

---

## 🏗️ Medallion Architecture

| Layer   | Description |
|--------|------------|
| 🥉 Bronze | Raw CSV data stored in S3 |
| 🥈 Silver | Cleaned, deduplicated, validated data |
| 🥇 Gold   | Business-ready aggregations |

---

## 📊 Key Features

- 🔄 End-to-end automated pipeline  
- 📦 Processes 10,000+ daily records  
- 🧪 12 data quality tests (dbt)  
- ⚡ 8-task Airflow DAG orchestration  
- 📈 Business insights generation:
  - Revenue by zone  
  - Driver performance  
  - Hourly demand  
  - Surge analysis  

---

## 🧰 Tech Stack

| Category        | Tools |
|----------------|------|
| Language        | Python, SQL |
| Processing      | Pandas / PySpark |
| Storage         | AWS S3 |
| Warehouse       | PostgreSQL (RDS) |
| Transformation  | dbt |
| Orchestration   | Apache Airflow |
| Visualization   | Streamlit |

---

## 📂 Project Structure


uber-trip-pipeline/
│
├── data/
│ ├── raw/ # Input CSV files
│ └── processed/ # Silver & Gold outputs
│
├── dags/
│ └── uber_pipeline.py # Airflow DAG (8 tasks)
│
├── scripts/
│ ├── bronze_to_silver.py # Data cleaning
│ ├── silver_to_gold.py # Aggregations
│ └── dashboard.py # Streamlit dashboard
│
├── dbt/
│ ├── models/ # SQL transformations
│ └── schema.yml # Data tests
│
├── docs/
│ └── index.html # Portfolio website
│
└── requirements.txt # Dependencies


---

## 📊 Sample Insights

- 💰 Top Revenue Zone: Airport ($49K+)  
- ⏰ Peak Demand Hour: Midnight  
- 🚗 Driver Performance Rankings  
- 📈 Daily Revenue Trends  
- ⚡ Surge Pricing Analysis  

---

## 🚀 Run Locally

```bash
# Clone repo
git clone https://github.com/SubhikshaRavichandran/uber-trip-pipeline.git
cd uber-trip-pipeline

# Install dependencies
pip install -r requirements.txt

# Run transformations
python scripts/bronze_to_silver.py
python scripts/silver_to_gold.py

# Run dashboard
streamlit run scripts/dashboard.py
