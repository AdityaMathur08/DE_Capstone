from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


# Initializing a Spark Session
spark = SparkSession \
    .builder \
    .appName("ClickStream_From_Kafka") \
    .getOrCreate()
spark.sparkContext.setLoglevel("ERROR")

# Host , port and topic configs
host = "18.211.252.152"
port = "9092"
topic = "de-capstone3"

# Reading Click Stream data from Kafka
clickStream_raw =spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", host +":"+port) \
        .option("startingOffsets", "latest") \
        .option("subscribe", topic) \
        .option("failOnDataLoss", False) \
        .load()

# Defining Schema of a single record
json_schema = StructType([StructField("customer_id",IntegerType()), 
                         StructField("app_version",StringType()),
                         StructField("os_version",StringType()),
                         StructField("lat",FloatType()),
                         StructField("lon",FloatType()),
                         StructField("page_id",StringType()),
                         StructField("button_id",StringType()),
                         StructField("is_button_click",StringType()),
                         StructField("is_page_view",StringType()),
                         StructField("is_scroll_up",StringType()),
                         StructField("is_scroll_down",StringType()),
                         StructField("timestamp",TimeStampType())])

#
clickstream = clickStream_raw.select(from_json(col("value").cast("string"),json_schema).alias("data")).select("data.*")

query = clickstream \
        .writeStream \
        .format("csv") \
        .outputMode("append") \
        .option("truncate","false") \
        .option("path","ClickStreamData") \
        .option("checkpointLocation","ClickStreamData_CHK_PNT") \
        .start()

query.awaitTermination()


# To Start running the script on spark cluster command:
# export SPARK_KAFKA_VERSION=0.10
# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5 task_01-Click_Stream_From_Kafka.py