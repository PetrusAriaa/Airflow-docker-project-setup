import datetime as dt
import pandas as pd

def Extract() -> tuple:
    print("Extracting data...")
    YGStock_path = f"frames/{dt.datetime.now().strftime('%Y-%m-%d_YGStock')}.csv"
    trend_path = f"frames/{dt.datetime.now().strftime('%Y-%m-%d_search-trend')}.csv"

    YG_df = pd.read_csv(YGStock_path)
    trend_df = pd.read_csv(trend_path)
    return YG_df, trend_df