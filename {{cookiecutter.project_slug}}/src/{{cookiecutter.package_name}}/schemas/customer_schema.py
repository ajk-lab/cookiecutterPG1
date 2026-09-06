from pyspark.sql.types import StructType, StructField, StringType

customer_schema = StructType([
    StructField("customer_id", StringType(), True),
    StructField("customer_name", StringType(), True),
])
