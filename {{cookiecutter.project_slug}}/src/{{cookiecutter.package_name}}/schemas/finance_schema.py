from pyspark.sql.types import StructType, StructField, StringType, DoubleType

finance_schema = StructType([
    StructField("gl_account", StringType(), True),
    StructField("amount", DoubleType(), True),
])
