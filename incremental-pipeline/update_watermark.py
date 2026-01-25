from pyspark.sql.functions import max
from pyspark.sql import Row

new_watermark = (
    df_incremental
    .select(max("subscription_date"))
    .collect()[0][0]
)

df_new_watermark = spark.createDataFrame(
    [Row(entity="customers", last_processed_date=new_watermark)]
)

watermark_path = "abfss://metadata@<storage-account>.dfs.core.windows.net/watermark_customers.csv"

df_new_watermark.write.mode("overwrite").option("header", "true").csv(watermark_path)
