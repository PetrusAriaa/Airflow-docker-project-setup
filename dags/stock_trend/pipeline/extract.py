import datetime as dt

def Extract(spark) -> tuple:
    print("Extracting data...")
    YGStock_path = f"frames/{dt.datetime.now().strftime('%Y-%m-%d_YGStock')}.csv"
    trend_path = f"frames/{dt.datetime.now().strftime('%Y-%m-%d_search-trend')}.csv"

    YG_df = spark.read.csv(YGStock_path, header=True)
    trend_df = spark.read.csv(trend_path, header=True)
    return YG_df, trend_df