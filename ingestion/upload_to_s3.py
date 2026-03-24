import boto3
import os
from datetime import datetime

# Config
BUCKET_NAME = "uber-trip-pipeline-sujith"
DATE_PREFIX = datetime.now().strftime("year=%Y/month=%m/day=%d")

s3 = boto3.client('s3', region_name='us-east-1')

def upload_file(local_path, s3_key):
    print(f"Uploading {local_path} → s3://{BUCKET_NAME}/{s3_key}")
    s3.upload_file(local_path, BUCKET_NAME, s3_key)
    print(f"✅ Uploaded successfully!")

# Upload raw files to Bronze layer with date partitioning
files = {
    'data/raw/trips.csv':     f'bronze/trips/{DATE_PREFIX}/trips.csv',
    'data/raw/drivers.csv':   f'bronze/drivers/{DATE_PREFIX}/drivers.csv',
    'data/raw/customers.csv': f'bronze/customers/{DATE_PREFIX}/customers.csv',
}

print(f"\n🚀 Uploading to S3 Bronze Layer...")
print(f"   Bucket: {BUCKET_NAME}")
print(f"   Date partition: {DATE_PREFIX}\n")

for local_path, s3_key in files.items():
    upload_file(local_path, s3_key)

# Verify uploads
print("\n📂 Verifying S3 Bronze Layer contents:")
response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix='bronze/')
for obj in response.get('Contents', []):
    size_kb = obj['Size'] / 1024
    print(f"   ✅ {obj['Key']} ({size_kb:.1f} KB)")

print("\n🎉 Bronze Layer upload complete!")
