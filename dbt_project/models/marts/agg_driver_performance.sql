
with trips as (
    select * from {{ ref('fct_trips') }}
),
drivers as (
    select * from {{ ref('stg_drivers') }}
),
performance as (
    select
        t.driver_id,
        d.driver_name,
        d.vehicle_type,
        d.city,
        d.driver_rating,
        count(t.trip_id)                       as total_trips,
        sum(t.completed_flag)                  as completed_trips,
        sum(t.cancelled_flag)                  as cancelled_trips,
        round(sum(t.total_amount)::numeric, 2) as total_earnings,
        round(avg(t.total_amount)::numeric, 2) as avg_earning_per_trip,
        round(avg(t.distance_miles)::numeric, 2) as avg_distance,
        round(
            sum(t.completed_flag)::numeric /
            nullif(count(t.trip_id), 0) * 100, 1
        ) as completion_rate_pct
    from trips t
    left join drivers d on t.driver_id = d.driver_id
    group by t.driver_id, d.driver_name, d.vehicle_type, d.city, d.driver_rating
)
select * from performance
order by total_earnings desc
