from pyspark.sql.functions import col
from delta.tables import DeltaTable

# Read bronze data
bronze_path = "abfss://bronze@<storage-account>.dfs.core.windows.net/customers-100.csv"

df_bronze = (
    spark.read
    .option("header", "true")
    .csv(bronze_path)
)

# Standardize columns
df_incremental = df_bronze.select(
    [col(c).alias(c.lower().replace(" ", "_")) for c in df_bronze.columns]
)

# Filter incremental records
df_incremental = df_incremental.filter(
    col("subscription_date") > last_processed_date
)

# Load Delta Silver
silver_delta_path = "abfss://silver@<storage-account>.dfs.core.windows.net/customers_delta"
delta_silver = DeltaTable.forPath(spark, silver_delta_path)

# MERGE
delta_silver.alias("silver").merge(
    df_incremental.alias("updates"),
    "silver.customer_id = updates.customer_id"
).whenNotMatchedInsertAll().execute()
