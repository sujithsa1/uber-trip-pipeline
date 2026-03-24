
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    pickup_zone as unique_field,
    count(*) as n_records

from "uber_trips"."analytics_analytics"."agg_zone_revenue"
where pickup_zone is not null
group by pickup_zone
having count(*) > 1



  
  
      
    ) dbt_internal_test