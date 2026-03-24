import pandas as pd
from sqlalchemy import create_engine, text
import time

DB_URL = "postgresql://uberadmin:UberTrip2026!@uber-trips-db.c0rwmgkciat4.us-east-1.rds.amazonaws.com:5432/uber_trips"
engine = create_engine(DB_URL)

def load_table(df, table_name):
    with engine.connect() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS public.{table_name} CASCADE"))
        conn.commit()
    time.sleep(1)
    df.to_sql(table_name, engine, schema="public", if_exists="replace", index=False)
    print(f"   ✅ {table_name}: {len(df)} rows loaded")

print("🚀 Loading data to PostgreSQL...")

df_trips = pd.read_parquet("data/processed/silver_trips/trips.parquet")
load_table(df_trips, "raw_trips")

df_drivers = pd.read_parquet("data/processed/silver_drivers/drivers.parquet")
load_table(df_drivers, "raw_drivers")

df_customers = pd.read_parquet("data/processed/silver_customers/customers.parquet")
load_table(df_customers, "raw_customers")

df_daily = pd.read_csv("data/processed/gold_daily_summary.csv")
load_table(df_daily, "gold_daily_summary")

df_zone = pd.read_csv("data/processed/gold_zone_performance.csv")
load_table(df_zone, "gold_zone_performance")

df_hourly = pd.read_csv("data/processed/gold_hourly_demand.csv")
load_table(df_hourly, "gold_hourly_demand")

df_driver = pd.read_csv("data/processed/gold_driver_performance.csv")
load_table(df_driver, "gold_driver_performance")

print("=" * 50)
print("🎉 All data loaded to PostgreSQL!")
print("=" * 50)
