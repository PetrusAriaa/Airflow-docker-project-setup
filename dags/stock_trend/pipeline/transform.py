from pyspark.sql.functions import col, from_utc_timestamp, date_format, to_date

def Transform(YG_df, trend_df):
    print("Running data transform...")
    # Remove columns 'Volume', 'Dividends', 'Stock Splits'
    columns_to_remove = ['Volume', 'Dividends', 'Stock Splits']
    YG_df = YG_df.drop(*columns_to_remove)
    YG_df = YG_df \
                .withColumn("Date", from_utc_timestamp(col("Date"), "Asia/Jakarta")) \
                .withColumn("Date", date_format(col("Date"), "yyyy-MM-dd"))
    trend_df = trend_df \
                    .withColumn("date", from_utc_timestamp(col("date"), "Asia/Jakarta")) \
                    .withColumn("date", date_format(col("date"), "yyyy-MM-dd")) \
                    .withColumnRenamed("Blackpink", "Frequency") \
                    .withColumnRenamed("date", "Date")

    joined = YG_df.join(trend_df, on="Date")
    
    
    # adjust column's dtype
    joined = joined.withColumn("Date", to_date(col("date"), "yyyy-MM-dd"))
    column_mapper = {"Open":"float", "High":"float", "Low":"float", "Close":"float", "Frequency":"integer"}
    
    for column, target_dtype in column_mapper.items():
        joined = joined.withColumn(column, col(column).cast(target_dtype))
    print("\n ==== RESULT ====")
    print(f"joined rows: {joined.count()}")
    joined.show()
    print(joined.dtypes)

    return joined