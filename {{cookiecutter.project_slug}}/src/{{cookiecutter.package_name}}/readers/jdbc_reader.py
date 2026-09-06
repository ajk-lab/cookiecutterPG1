def read_jdbc(spark, url, table, properties=None):
    properties = properties or {}
    return spark.read.jdbc(url=url, table=table, properties=properties)
