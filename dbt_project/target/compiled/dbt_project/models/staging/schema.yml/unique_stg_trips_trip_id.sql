
    
    

select
    trip_id as unique_field,
    count(*) as n_records

from "uber_trips"."analytics_staging"."stg_trips"
where trip_id is not null
group by trip_id
having count(*) > 1


