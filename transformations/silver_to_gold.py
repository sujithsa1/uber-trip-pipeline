import pandas as pd
import os

print("✅ Starting Gold Layer transformation (pandas)")

os.makedirs("data/processed", exist_ok=True)

df = pd.read_parquet("data/processed/silver_trips/trips.parquet")
print(f"📂 Loaded {len(df)} silver trip records")

df["pickup_time"] = pd.to_datetime(df["pickup_time"])
df["trip_date"] = df["pickup_time"].dt.date
df["hour_of_day"] = df["pickup_time"].dt.hour

print("🔄 Building Daily Revenue Summary...")
gold_daily = df.groupby("trip_date").agg(
    total_trips=("trip_id", "count"),
    completed_trips=("completed_flag", "sum"),
    cancelled_trips=("cancelled_flag", "sum"),
    total_revenue=("total_amount", "sum"),
    avg_fare=("fare_amount", "mean"),
    avg_duration=("trip_duration_minutes", "mean"),
    avg_distance=("distance_miles", "mean"),
    avg_tip=("tip_amount", "mean")
).round(2).reset_index()
gold_daily.to_csv("data/processed/gold_daily_summary.csv", index=False)
print(f"   ✅ Daily summary: {len(gold_daily)} days")

print("🔄 Building Zone Revenue Performance...")
gold_zone = df[df["completed_flag"]==1].groupby("pickup_zone").agg(
    total_trips=("trip_id", "count"),
    total_revenue=("total_amount", "sum"),
    avg_revenue_per_trip=("total_amount", "mean"),
    avg_distance=("distance_miles", "mean"),
    avg_duration=("trip_duration_minutes", "mean"),
    avg_surge=("surge_multiplier", "mean")
).round(2).reset_index().sort_values("total_revenue", ascending=False)
gold_zone.to_csv("data/processed/gold_zone_performance.csv", index=False)
print(f"   ✅ Zone performance: {len(gold_zone)} zones")

print("🔄 Building Hourly Demand...")
gold_hourly = df.groupby("hour_of_day").agg(
    total_trips=("trip_id", "count"),
    completed_trips=("completed_flag", "sum"),
    total_revenue=("total_amount", "sum"),
    avg_surge=("surge_multiplier", "mean")
).round(2).reset_index()
gold_hourly.to_csv("data/processed/gold_hourly_demand.csv", index=False)
print(f"   ✅ Hourly demand: {len(gold_hourly)} hours")

print("🔄 Building Driver Performance...")
gold_driver = df.groupby("driver_id").agg(
    total_trips=("trip_id", "count"),
    completed_trips=("completed_flag", "sum"),
    cancelled_trips=("cancelled_flag", "sum"),
    total_earnings=("total_amount", "sum"),
    avg_earning_per_trip=("total_amount", "mean"),
    avg_distance=("distance_miles", "mean")
).round(2).reset_index()
gold_driver["completion_rate"] = (gold_driver["completed_trips"] / gold_driver["total_trips"] * 100).round(1)
gold_driver = gold_driver.sort_values("total_earnings", ascending=False)
gold_driver.to_csv("data/processed/gold_driver_performance.csv", index=False)
print(f"   ✅ Driver performance: {len(gold_driver)} drivers")

print("🔄 Building Surge Analysis...")
gold_surge = df.groupby("surge_multiplier").agg(
    total_trips=("trip_id", "count"),
    total_revenue=("total_amount", "sum"),
    avg_fare=("total_amount", "mean"),
    cancellations=("cancelled_flag", "sum")
).round(2).reset_index()
gold_surge.to_csv("data/processed/gold_surge_analysis.csv", index=False)
print(f"   ✅ Surge analysis complete")

print("=" * 50)
print("🎉 Gold Layer Complete!")
print("=" * 50)
