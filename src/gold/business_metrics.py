import json
from pyspark.sql.functions import sum
from src.common.spark_session import get_spark

spark = get_spark()

with open("config/config.json") as f:
    config = json.load(f)

df = spark.read.format("delta").load(config["paths"]["silver"])

df_gold = df.groupBy("category").agg(sum("amount").alias("total_spent"))

df_gold.write.format("delta").mode("overwrite").save(config["paths"]["gold"])

print("Gold complete")
