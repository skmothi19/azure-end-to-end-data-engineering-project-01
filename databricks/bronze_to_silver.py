from pyspark.sql.functions import col

bronze_path = "abfss://bronze@<storage-account>.dfs.core.windows.net/customers-100.csv"
silver_path = "abfss://silver@<storage-account>.dfs.core.windows.net/customers"

df_bronze = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load(bronze_path)
)

df_silver = df_bronze.select(
    [col(c).alias(c.lower().replace(" ", "_")) for c in df_bronze.columns]
)

df_silver_clean = df_silver.filter(col("email").isNotNull())

df_silver_clean.write.mode("overwrite").format("parquet").save(silver_path)
