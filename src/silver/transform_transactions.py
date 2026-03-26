import json
from pyspark.sql.functions import col
from src.common.spark_session import get_spark

spark = get_spark()

with open("config/config.json") as f:
    config = json.load(f)

df = spark.read.format("delta").load(config["paths"]["bronze"])

df_clean = df.dropDuplicates(["transaction_id"]) \
    .filter(col("amount").isNotNull())

df_clean.write.format("delta").mode("overwrite").save(config["paths"]["silver"])

print("Silver complete")
