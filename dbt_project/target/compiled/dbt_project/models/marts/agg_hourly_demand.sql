with trips as (
    select * from "uber_trips"."analytics_analytics"."fct_trips"
),
hourly as (
    select
        pickup_hour,
        count(trip_id)                         as total_trips,
        sum(completed_flag)                    as completed_trips,
        round(sum(total_amount)::numeric, 2)   as total_revenue,
        round(avg(surge_multiplier)::numeric, 2) as avg_surge,
        round(avg(trip_duration_minutes)::numeric, 2) as avg_duration
    from trips
    group by pickup_hour
)
select * from hourly
order by pickup_hour