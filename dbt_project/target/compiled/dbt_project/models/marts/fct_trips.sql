with trips as (
    select * from "uber_trips"."analytics_staging"."stg_trips"
),
final as (
    select
        trip_id,
        driver_id,
        customer_id,
        vehicle_type,
        pickup_zone,
        dropoff_zone,
        pickup_time,
        dropoff_time,
        date(pickup_time)            as trip_date,
        extract(hour from pickup_time) as pickup_hour,
        extract(dow from pickup_time)  as day_of_week,
        trip_duration_minutes,
        distance_miles,
        fare_amount,
        tip_amount,
        surge_multiplier,
        total_amount,
        payment_type,
        trip_status,
        completed_flag,
        cancelled_flag
    from trips
)
select * from final