import pandas as pd
import os

print("✅ Starting Silver Layer transformation (pandas)")

# Read raw data
print("🔄 Processing Trips...")
df_trips = pd.read_csv("data/raw/trips.csv")

# Clean trips
df_trips = df_trips.drop_duplicates(subset=["trip_id"])
df_trips["pickup_zone"] = df_trips["pickup_zone"].str.upper().str.strip()
df_trips["dropoff_zone"] = df_trips["dropoff_zone"].str.upper().str.strip()
df_trips["trip_status"] = df_trips["trip_status"].str.strip()
df_trips["distance_miles"] = pd.to_numeric(df_trips["distance_miles"], errors="coerce")
df_trips["fare_amount"] = pd.to_numeric(df_trips["fare_amount"], errors="coerce")
df_trips["tip_amount"] = pd.to_numeric(df_trips["tip_amount"], errors="coerce").fillna(0)
df_trips["total_amount"] = pd.to_numeric(df_trips["total_amount"], errors="coerce")
df_trips["surge_multiplier"] = pd.to_numeric(df_trips["surge_multiplier"], errors="coerce").fillna(1.0)
df_trips["completed_flag"] = (df_trips["trip_status"] == "completed").astype(int)
df_trips["cancelled_flag"] = (df_trips["trip_status"] == "cancelled").astype(int)
df_trips = df_trips[df_trips["distance_miles"] > 0]
df_trips = df_trips[df_trips["fare_amount"] >= 0]

os.makedirs("data/processed/silver_trips", exist_ok=True)
df_trips.to_parquet("data/processed/silver_trips/trips.parquet", index=False)
print(f"   ✅ Trips saved: {len(df_trips)} rows")

print("🔄 Processing Drivers...")
df_drivers = pd.read_csv("data/raw/drivers.csv")
df_drivers = df_drivers.drop_duplicates(subset=["driver_id"])
df_drivers["city"] = df_drivers["city"].str.upper().str.strip()
df_drivers["driver_rating"] = pd.to_numeric(df_drivers["driver_rating"], errors="coerce")
df_drivers = df_drivers[df_drivers["driver_id"].notna()]

os.makedirs("data/processed/silver_drivers", exist_ok=True)
df_drivers.to_parquet("data/processed/silver_drivers/drivers.parquet", index=False)
print(f"   ✅ Drivers saved: {len(df_drivers)} rows")

print("🔄 Processing Customers...")
df_customers = pd.read_csv("data/raw/customers.csv")
df_customers = df_customers.drop_duplicates(subset=["customer_id"])
df_customers["city"] = df_customers["city"].str.upper().str.strip()
df_customers = df_customers[df_customers["customer_id"].notna()]

os.makedirs("data/processed/silver_customers", exist_ok=True)
df_customers.to_parquet("data/processed/silver_customers/customers.parquet", index=False)
print(f"   ✅ Customers saved: {len(df_customers)} rows")

print("=" * 50)
print("🎉 Silver Layer Complete!")
print("   📂 Location: data/processed/silver_*/")
print("=" * 50)
