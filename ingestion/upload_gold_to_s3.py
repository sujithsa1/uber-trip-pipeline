import boto3
import os
from datetime import datetime

BUCKET = "uber-trip-pipeline-sujith"
DATE_PREFIX = datetime.now().strftime("year=%Y/month=%m/day=%d")
s3 = boto3.client("s3", region_name="us-east-1")

gold_files = {
    "data/processed/gold_daily_summary.csv":    f"gold/daily_summary/{DATE_PREFIX}/gold_daily_summary.csv",
    "data/processed/gold_zone_performance.csv": f"gold/zone_performance/{DATE_PREFIX}/gold_zone_performance.csv",
    "data/processed/gold_hourly_demand.csv":    f"gold/hourly_demand/{DATE_PREFIX}/gold_hourly_demand.csv",
    "data/processed/gold_driver_performance.csv": f"gold/driver_performance/{DATE_PREFIX}/gold_driver_performance.csv",
    "data/processed/gold_surge_analysis.csv":   f"gold/surge_analysis/{DATE_PREFIX}/gold_surge_analysis.csv",
}

print("🚀 Uploading Gold Layer to S3...\n")
for local_path, s3_key in gold_files.items():
    print(f"   Uploading {local_path}...")
    s3.upload_file(local_path, BUCKET, s3_key)
    print(f"   ✅ Done!")

print("\n📂 Verifying S3 Gold Layer:")
response = s3.list_objects_v2(Bucket=BUCKET, Prefix="gold/")
for obj in response.get("Contents", []):
    size_kb = obj["Size"] / 1024
    print(f"   ✅ {obj['Key']} ({size_kb:.1f} KB)")

print("\n🎉 All Gold data uploaded to S3!")
