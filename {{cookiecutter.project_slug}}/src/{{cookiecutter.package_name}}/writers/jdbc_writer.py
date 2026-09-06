def write_jdbc(df, url, table, mode="overwrite", properties=None):
    properties = properties or {}
    df.write.jdbc(url=url, table=table, mode=mode, properties=properties)
