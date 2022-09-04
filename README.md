DE_CAPSTONE
In this project, you will ingest data using both real-time and batch frameworks and load them into tables. Once that is complete, you will write queries to derive meaningful insights from them


Basically we need to onboard data on more scalable platform and build analytical solutions on top of it.


Suppose you are working at a mobility start-up company called ‘YourOwnCabs’ (YOC). Primarily, it is an online on-demand cab booking service. When you joined the company, it was doing around 100 rides per day. Owing to a successful business model and excellent service, the company’s business is growing rapidly, and these numbers are breaking their own records every day. YOC’s customer base and ride counts are increasing on a day-by-day basis. 

highly important for business stakeholders to derive quick and on-demand insights regarding the numbers to decide the company’s future strategy. Owing to the massive growth in business, it is getting tough for the company’s management to obtain the business numbers frequently, as backend MySQL is not capable of catering to all types of queries owing to large volume data. The following statistics will help you understand the gravity of the situation:





With a rising number of users and rides, the company’s major focus is to provide its customers a delightful experience while ensuring zero downtime

business stakeholders should be catered with all the answers that they require that are backed by data. Data-driven decisions play a steroid role for a fast-growing start-up.

as a big data engineer, must architect and build a solution to cater to the following requirements:
 
1. Booking data analytics solution: This is a feature in which the ride-booking data is stored in a way such that it is available for all types of analytics without hampering business. These analyses mostly include daily, weekly and monthly booking counts as well as booking counts by the mobile operating system, average booking amount, total tip amount, etc.
2. Clickstream data analytics solution: Clickstream is the application browsing data that is generated on every action taken by the user on the app. This includes link click, button click, screen load, etc. This is relevant to know the user’s intent and then take action to engage them more in the app according to their browsing behaviour. Since this is very high-volume data (more than the bookings data), it needs to be architectured quite well and stored in a proper format for analysis.


Data




following data will be used for this problem:
bookings (The booking data is added to/updated in this table after a booking/ride is successfully completed.) 

• booking_id: Booking ID String
• customer_id: Customer ID Number
• driver_id: Driver ID Number
• customer_app_version: Customer App Version String
• customer_phone_os_version: Customer mobile operating system
• pickup_lat: Pickup latitude
• pickup_lon: Pickup longitude
• drop_lat: Dropoff latitude
• drop_lon: Dropoff longitude
• pickup_timestamp: Timestamp at which customer was picked up
• drop_timestamp: Timestamp at which customer was dropped at destination
• trip_fare: Total amount of the trip
• tip_amount: Tip amount given by customer to driver for this ride
• currency_code: Currency Code String for the amount paid by customer
• cab_color: Color of the cab
• cab_registration_no: Registration number string of the vehicle
• customer_rating_by_driver: Rating number given by driver to customer after ride
• rating_by_customer: Rating number given by customer to driver after ride
• passenger_count: Total count of passengers who boarded the cab for ride

Since booking data is updated by the backend team in MySQL, it is stored in a central AWS RDS. You will be given the already loaded bookings table data.

clickstream (All user’s activity data such as click and page load):

• customer_id: Customer ID Number
• app_version: Customer App Version String
• os_version: User mobile operating system
• lat: Latitude
• lon: Longitude
• page_id: UUID of the page/screen browsed by a user
• button_id: UUID of the button clicked by a user
• is_button_click: Yes/No depending on whether a user clicked button
• is_page_view: Yes/No depending on whether a user loaded a new screen/page
• is_scroll_up: Yes/No depending on whether a user scrolled up on the current screen
• is_scroll_down: Yes/No depending on whether a user scrolled down on the current screen
• timestamp: Timestamp at which the user action is captured

This data is the real-time streaming data generated by the application in the JSON format. It is stored in an existing Kafka server. You will be given the already loaded clickstream Kafka Topic.


Here is an example of a JSON payload structure that is produced:
{
  "customer_id": 342516,
  "app_version": "4.1.34-beta",
  "OS_version": "Android",
  "lat": 14.11,
  "lon": 89.88,
  "page_id": "e7bc5fb2-1231-11eb-adc1-0242ac120002",
  "button_id": "fcba68aa-1231-11eb-adc1-0242ac120002",
  "is_button_click": yes,
  "is_page_view": no,
  "is_scroll_up": no,
  "is_scroll_down": no,
  "timestamp": "2020-10-20TT17:52:24"}


