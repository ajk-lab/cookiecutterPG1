def count_duplicates(df, key_columns):
    return (
        df.groupBy(*key_columns)
        .count()
        .filter("count > 1")
        .count()
    )
