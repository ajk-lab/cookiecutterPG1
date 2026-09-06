def read_parquet(spark, path):
    return spark.read.parquet(path)
