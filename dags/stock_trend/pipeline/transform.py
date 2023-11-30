import pandas as pd


def Transform(YG_df: pd.DataFrame, trend_df: pd.DataFrame):
    print("Running data transform...")
    # Remove columns 'Volume', 'Dividends', 'Stock Splits'
    columns_to_remove = ['Volume', 'Dividends', 'Stock Splits']
    YG_df = YG_df.drop(columns_to_remove, axis=1)
    YG_df['Date'] = pd.to_datetime(YG_df['Date'])
    trend_df['date'] = pd.to_datetime(trend_df['date'])
    
    YG_df['Date'].dt.tz_convert('Asia/Jakarta')
    trend_df['date'] = trend_df['date'].dt.tz_localize('utc').dt.tz_convert('Asia/Jakarta')

    YG_df['Date'] = YG_df['Date'].dt.strftime('%Y-%m-%d')
    trend_df['date'] = trend_df['date'].dt.strftime('%Y-%m-%d')
    
    trend_df = trend_df.rename(columns={"Blackpink": "Frequency", "date": "Date"})    
    
    YG_df = YG_df.astype({"Open": float, "High": float, "Low": float, "Close": float})
    YG_df['Date'] = pd.to_datetime(YG_df['Date'])
    trend_df['Date'] = pd.to_datetime(trend_df['Date'])

    joined = pd.merge(YG_df, trend_df, on='Date')
    joined['Date'] = pd.to_datetime(joined['Date'])

    print("\n ==== RESULT ====")
    print(f"joined rows: {joined.shape[0]}")
    print(joined.head(4))
    print(joined.dtypes)

    return joined