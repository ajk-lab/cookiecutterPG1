def read_csv(spark, path, **options):
    return spark.read.options(**options).csv(path, header=True, inferSchema=True)
