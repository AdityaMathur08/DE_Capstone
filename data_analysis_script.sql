use capstone;


-- Task 5: Calculate the total number of different drivers for each customer.

SELECT customer_id,
COUNT(driver_id) AS Number_of_drivers
FROM bookings
group by customer_id;

-- Task 6: Calculate the total rides taken by each customer.

SELECT customer_id,
COUNT(booking_id) AS Number_of_rides_taken
FROM bookings
group by customer_id;

-- Task 7:  total visits made by each customer on the booking page and the total ‘Book Now’ button presses.

SELECT * FROM clickstream LIMIT 10;


with temp_table AS(
SELECT 
CASE WHEN is_button_click = 'Yes' THEN 1 ELSE 0 END AS is_button_bool,
CASE WHEN is_page_view = 'Yes' THEN 1 ELSE 0 END AS is_page_view_bool
FROM clickstream
)
SELECT SUM(is_button_bool)/SUM(is_page_view_bool) AS conversion_raio 
FROM temp_table;

-- TASK 08 : Calculate the count of all trips done on black cabs.


SELECT cab_color, COUNT(booking_id)
FROM bookings
GROUP BY cab_color
HAVING cab_color = 'black';

-- Task 9: Calculate the total amount of tips given date wise to all drivers by customers.

SELECT date(drop_timestamp)AS Booking_Date,
SUM(trip_amount) as tip_amount
FROM bookings
GROUP BY date(drop_timestamp);

-- TASK 10 : Calculate the total count of all the bookings with ratings lower than 2 as given by customers in a particular month

SELECT concat(year(drop_timestamp),'-',month(drop_timestamp)) AS booking_month,
COUNT(booking_id) AS low_ratings_bookings
FROM bookings
WHERE rating_by_customer < 2
GROUP BY concat(year(drop_timestamp),'-',month(drop_timestamp))
ORDER BY low_ratings_bookings DESC;

-- Task 11: Calculate the count of total iOS users.

SELECT 
COUNT(*) AS iOS_Users
FROM bookings
WHERE customer_phone_os_version = 'iOS';


