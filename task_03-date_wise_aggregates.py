import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import unix_timestamp, from_unixtime


spark = SparkSession.builder.master("local").appName("datewise_booking").getOrCreate()
sc = spark.sparkContext
sc

stream_df = spark.read.csv("/user/hadoop/Capstone/ClickStreamData/part-00000-7171026c-78d5-443d-9047-f0aab83e8305-c000.csv",inferSchema = True)


stream_df = stream_df.withColumnRenamed("_c0","customer_id")\
         .withColumnRenamed("_c1","app_version")\
         .withColumnRenamed("_c2","os_version") \
         .withColumnRenamed("_c3","lat") \
         .withColumnRenamed("_c4","lon") \
         .withColumnRenamed("_c5","page_id") \
         .withColumnRenamed("_c6","button_id") \
         .withColumnRenamed("_c7","is_button_click") \
         .withColumnRenamed("_c8","is_page_view") \
         .withColumnRenamed("_c9","is_scroll_up") \
         .withColumnRenamed("_c10","is_scroll_down") \
         .withColumnRenamed("_c11","timestamp") \


batch_df = spark.read.csv('/user/hadoop/Capstone/Bookings_Batch_data/part-m-00000',inferSchema = True)

batch_df = batch_df.withColumnRenamed("_c0","booking_id")\
	   .withColumnRenamed("_c1","customer_id") \
	   .withColumnRenamed("_c2","driver_id") \
	   .withColumnRenamed("_c3","customer_app_version")  \
	   .withColumnRenamed("_c4","customer_phone_os_version") \
	   .withColumnRenamed("_c5","pickup_lat") \
	   .withColumnRenamed("_c6","pickup_lon") \
	   .withColumnRenamed("_c7","drop_lat") \
	   .withColumnRenamed("_c8","drop_lon") \
	   .withColumnRenamed("_c9","pickup_timestamp")  \
	   .withColumnRenamed("_c10","drop_timestamp")  \
	   .withColumnRenamed("_c11","trip_fare") \
	   .withColumnRenamed("_c12","tip_amount")  \
	   .withColumnRenamed("_c13","currency_code") \
	   .withColumnRenamed("_c14","cab_color")  \
	   .withColumnRenamed("_c15","cab_registration_no") \
	   .withColumnRenamed("_c16","customer_rating_by_driver")  \
	   .withColumnRenamed("_c17","rating_by_customer")  \
	   .withColumnRenamed("_c18","passenger_count")

batch_df =  batch_df.withColumn("date", date_format('pickup_timestamp', "yyyy-MM-dd"))

date_agg = batch_df.groupBy('date').count()

date_agg.coalesce(1).write.format('com.databricks.spark.csv').mode('overwrite').save('/user/hadoop/Capstone/aggregations/', header = 'true')
