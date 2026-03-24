
    
    

with all_values as (

    select
        trip_status as value_field,
        count(*) as n_records

    from "uber_trips"."analytics_staging"."stg_trips"
    group by trip_status

)

select *
from all_values
where value_field not in (
    'completed','cancelled'
)


