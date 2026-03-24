
  create view "uber_trips"."analytics_staging"."stg_customers__dbt_tmp"
    
    
  as (
    with source as (
    select * from public.raw_customers
),
cleaned as (
    select
        customer_id,
        city,
        signup_date::date as signup_date,
        loyalty_tier
    from source
    where customer_id is not null
)
select * from cleaned
  );