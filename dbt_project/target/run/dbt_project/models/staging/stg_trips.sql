
  create view "uber_trips"."analytics_staging"."stg_trips__dbt_tmp"
    
    
  as (
    with source as (
    select * from public.raw_trips
),
cleaned as (
    select
        trip_id,
        driver_id,
        customer_id,
        vehicle_type,
        pickup_zone,
        dropoff_zone,
        pickup_time::timestamp        as pickup_time,
        dropoff_time::timestamp       as dropoff_time,
        trip_duration_minutes::float  as trip_duration_minutes,
        distance_miles::float         as distance_miles,
        fare_amount::float            as fare_amount,
        tip_amount::float             as tip_amount,
        surge_multiplier::float       as surge_multiplier,
        total_amount::float           as total_amount,
        payment_type,
        trip_status,
        case when trip_status = 'completed' then 1 else 0 end as completed_flag,
        case when trip_status = 'cancelled' then 1 else 0 end as cancelled_flag
    from source
    where trip_id is not null
      and distance_miles > 0
      and fare_amount >= 0
)
select * from cleaned
  );