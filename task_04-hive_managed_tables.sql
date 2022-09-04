
# Creating a database

CREATE DATABASE IF NOT EXISTS capstone;

DESCRIBE DATABASE EXTENDED capstone;

USE capstone;

-- Create a Hive Managed table for Clickstream data.
Create  table if not exists clickstream (
       customer_id String,
        app_version String,
        os_version String,
        lat String,
        lon String,
        page_id String,
        button_id String,
        is_button_click String,
        is_page_view String,
        is_scroll_up String,
        is_scroll_down String,
        `timestamp` String)
row format delimited 
fields terminated by ',' 
lines terminated by '\n'
stored as textfile;


Load data inpath '/user/hadoop/Capstone/ClickStreamData/part-00000-c132f8c8-2ff1-49ad-a199-24673e624285-c000.csv' into table clickstream;

-- Create Hive Managed table for bookings data:


Create  table if not exists bookings (
        booking_id String,
        customer_id String,
        driver_id String,
        customer_app_version String,
        customer_phone_os_version String,
        pickup_lat String,
        pickup_lon String,
        drop_lat String,
        drop_lon String,
        pickup_timestamp timestamp,
        drop_timestamp timestamp,
        trip_fare float,
        tip_amount float,
        currency_code String,
        cab_color String,
        cab_registration_number String,
        customer_rating_by_driver int,
        rating_by_customer int,
        passenger_count int)
row format delimited 
fields terminated by ',' 
lines terminated by '\n'
stored as textfile;

Load data inpath '/user/hadoop/Capstone/Bookings_Batch_data/part-m-00000' into table bookings;


-- Create a Hive-managed table for aggregated data in Task 3.

CREATE TABLE IF NOT EXISTS rides_aggregation (
        booking_date date,
        rides_booked int
)
row format delimited 
fields terminated by ',' 
lines terminated by '\n'
stored as textfile;

Load data inpath '/user/hadoop/Capstone/aggregations/part-00000-597eca41-05e8-4258-b4ac-17b1e267fe2e-c000.csv' into table rides_aggregation;