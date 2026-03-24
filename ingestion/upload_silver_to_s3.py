import boto3
import os

BUCKET = "uber-trip-pipeline-sujith"
s3 = boto3.client("s3", region_name="us-east-1")

def upload_folder(local_folder, s3_prefix):
    files = [f for f in os.listdir(local_folder) if not f.startswith(".")]
    for filename in files:
        local_path = os.path.join(local_folder, filename)
        s3_key = f"{s3_prefix}/{filename}"
        print(f"   Uploading {filename}...")
        s3.upload_file(local_path, BUCKET, s3_key)
    print(f"   ✅ {local_folder} uploaded!")

print("🚀 Uploading Silver Layer to S3...\n")
upload_folder("data/processed/silver_trips",     "silver/trips")
upload_folder("data/processed/silver_drivers",   "silver/drivers")
upload_folder("data/processed/silver_customers", "silver/customers")

print("\n📂 Verifying Full S3 Structure:")
for prefix in ["bronze/", "silver/", "gold/"]:
    response = s3.list_objects_v2(Bucket=BUCKET, Prefix=prefix)
    count = len(response.get("Contents", []))
    print(f"   ✅ {prefix:<10} → {count} files")

print("\n🎉 All 3 layers now in S3!")
