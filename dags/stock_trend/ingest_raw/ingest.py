import os
import time as t

from stock_trend.ingest_raw.stock import ExtractStock
from stock_trend.ingest_raw.trends import ExtractTrends

def validate_directory() -> None:
    if os.path.exists('frames'):
        print('directory ensured')
        return
    print('Directory does not exist')
    print(f'Creating {os.getcwd()}/frames')
    os.mkdir('frames')


def StartIngest():
    validate_directory()
    
    start = round(t.time()*1000)
    print("Fetching stock data...")
    stock_data = ExtractStock()
    print("Fetching trend data...")
    trend_data = ExtractTrends()
    end = round(t.time()*1000) - start
    print(f"Ingestion succeed in {end}ms")
    return stock_data, trend_data