import json
from pyspark.sql.functions import current_timestamp
from src.common.spark_session import get_spark

spark = get_spark()

with open("config/config.json") as f:
    config = json.load(f)

df = spark.read.csv(config["paths"]["raw"], header=True, inferSchema=True)

df = df.withColumn("ingestion_time", current_timestamp())

df.write.format("delta").mode("overwrite").save(config["paths"]["bronze"])

print("Bronze complete")
