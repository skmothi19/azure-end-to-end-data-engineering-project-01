from pyspark.sql.functions import col

# Read watermark metadata
watermark_path = "abfss://metadata@<storage-account>.dfs.core.windows.net/watermark_customers.csv"

df_watermark = (
    spark.read
    .option("header", "true")
    .csv(watermark_path)
)

last_processed_date = (
    df_watermark
    .filter(col("entity") == "customers")
    .select("last_processed_date")
    .collect()[0][0]
)

print("Last processed date:", last_processed_date)
