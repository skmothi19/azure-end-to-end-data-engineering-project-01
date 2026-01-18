from pyspark.sql.functions import count

silver_path = "abfss://silver@<storage-account>.dfs.core.windows.net/customers"
gold_path = "abfss://gold@<storage-account>.dfs.core.windows.net/customers_by_country"

df_silver = spark.read.parquet(silver_path)

df_gold = (
    df_silver
    .groupBy("country")
    .agg(count("customer_id").alias("customer_count"))
)

df_gold.write.mode("overwrite").format("parquet").save(gold_path)
