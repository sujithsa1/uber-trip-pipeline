with trips as (
    select * from "uber_trips"."analytics_analytics"."fct_trips"
    where completed_flag = 1
),
aggregated as (
    select
        pickup_zone,
        count(trip_id)            as total_trips,
        round(sum(total_amount)::numeric, 2)  as total_revenue,
        round(avg(total_amount)::numeric, 2)  as avg_revenue_per_trip,
        round(avg(distance_miles)::numeric, 2) as avg_distance,
        round(avg(trip_duration_minutes)::numeric, 2) as avg_duration_mins,
        round(avg(surge_multiplier)::numeric, 2) as avg_surge
    from trips
    group by pickup_zone
)
select * from aggregated
order by total_revenue desc