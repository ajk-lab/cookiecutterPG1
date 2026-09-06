def write_csv(df, path, mode="overwrite"):
    df.write.mode(mode).option("header", True).csv(path)
