
with source as (
    select * from public.raw_drivers
),
cleaned as (
    select
        driver_id,
        driver_name,
        vehicle_type,
        city,
        join_date::date      as join_date,
        driver_rating::float as driver_rating
    from source
    where driver_id is not null
)
select * from cleaned
