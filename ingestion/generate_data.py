import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()
random.seed(42)
np.random.seed(42)

NUM_TRIPS = 10000
NUM_DRIVERS = 200
NUM_CUSTOMERS = 500
ZONES = ["Downtown", "Airport", "Midtown", "Brooklyn", "Queens", "Bronx", "Harlem", "Staten Island"]
VEHICLE_TYPES = ["UberX", "UberXL", "UberBlack", "UberPool"]
PAYMENT_TYPES = ["credit_card", "debit_card", "cash", "wallet"]
STATUSES = ["completed", "completed", "completed", "cancelled"]

print("Generating trip data...")

drivers = []
for i in range(NUM_DRIVERS):
    drivers.append({
        "driver_id": f"DRV{1000+i}",
        "driver_name": fake.name(),
        "vehicle_type": random.choice(VEHICLE_TYPES),
        "city": random.choice(["New York", "Brooklyn", "Queens"]),
        "join_date": str(fake.date_between(start_date="-3y", end_date="-6m")),
        "driver_rating": round(random.uniform(3.5, 5.0), 1)
    })
pd.DataFrame(drivers).to_csv("data/raw/drivers.csv", index=False)
print(f"✅ Generated {NUM_DRIVERS} drivers")

customers = []
for i in range(NUM_CUSTOMERS):
    customers.append({
        "customer_id": f"CUST{10000+i}",
        "city": random.choice(["New York", "Brooklyn", "Queens"]),
        "signup_date": str(fake.date_between(start_date="-2y", end_date="-1m")),
        "loyalty_tier": random.choice(["Bronze", "Silver", "Gold", "Platinum"])
    })
pd.DataFrame(customers).to_csv("data/raw/customers.csv", index=False)
print(f"✅ Generated {NUM_CUSTOMERS} customers")

trips = []
for i in range(NUM_TRIPS):
    pickup_time = fake.date_time_between(start_date="-30d", end_date="now")
    duration = int(random.randint(5, 90))   # clean integer, no "s"
    dropoff_time = pickup_time + timedelta(minutes=duration)
    distance = round(float(random.uniform(0.5, 25.0)), 2)
    base_fare = round(distance * random.uniform(1.5, 3.5), 2)
    surge = float(random.choice([1.0, 1.0, 1.0, 1.2, 1.5, 2.0]))
    tip = round(float(random.uniform(0, 15)), 2)
    status = random.choice(STATUSES)

    trips.append({
        "trip_id": f"TRIP{100000+i}",
        "driver_id": f"DRV{random.randint(1000, 1000+NUM_DRIVERS-1)}",
        "customer_id": f"CUST{random.randint(10000, 10000+NUM_CUSTOMERS-1)}",
        "vehicle_type": random.choice(VEHICLE_TYPES),
        "pickup_zone": random.choice(ZONES),
        "dropoff_zone": random.choice(ZONES),
        "pickup_time": pickup_time.strftime("%Y-%m-%d %H:%M:%S"),
        "dropoff_time": dropoff_time.strftime("%Y-%m-%d %H:%M:%S"),
        "trip_duration_minutes": duration,
        "distance_miles": distance,
        "base_fare": base_fare,
        "surge_multiplier": surge,
        "fare_amount": round(base_fare * surge, 2),
        "tip_amount": tip if status == "completed" else 0.0,
        "total_amount": round(base_fare * surge + tip, 2) if status == "completed" else 0.0,
        "payment_type": random.choice(PAYMENT_TYPES),
        "trip_status": status
    })

df_trips = pd.DataFrame(trips)
df_trips.to_csv("data/raw/trips.csv", index=False)
print(f"✅ Generated {NUM_TRIPS} trips")
print(f"\n📊 Data Summary:")
print(f"   Total Trips:     {len(df_trips)}")
print(f"   Completed Trips: {len(df_trips[df_trips.trip_status=='completed'])}")
print(f"   Cancelled Trips: {len(df_trips[df_trips.trip_status=='cancelled'])}")
print(f"   Total Revenue:   ${df_trips.total_amount.sum():,.2f}")
print(f"   Avg Fare:        ${df_trips.fare_amount.mean():.2f}")
print(f"\n✅ Clean data saved to data/raw/")
