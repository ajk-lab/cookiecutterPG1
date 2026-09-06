def show_config(spark):
    for k, v in spark.sparkContext.getConf().getAll():
        print(f"{k} = {v}")
