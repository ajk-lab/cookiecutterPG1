from pyspark.sql.types import StructType, StructField, StringType, DoubleType

sales_schema = StructType([
    StructField("sale_id", StringType(), True),
    StructField("amount", DoubleType(), True),
])
