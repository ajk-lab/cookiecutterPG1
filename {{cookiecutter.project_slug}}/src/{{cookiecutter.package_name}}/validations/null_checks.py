def count_nulls(df, column_name):
    return df.filter(df[column_name].isNull()).count()
