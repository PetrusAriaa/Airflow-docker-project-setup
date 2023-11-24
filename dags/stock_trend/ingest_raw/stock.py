import yfinance as yf
import datetime as dt

TICKER_SYMBOL = '122870.KQ'

def ExtractStock() -> None:
    yg_stock = yf.Ticker(TICKER_SYMBOL)

    historical_data = yg_stock.history(period='1mo')

    FILE_NAME = f"frames/{dt.datetime.now().strftime('%Y-%m-%d_YGStock')}.csv"

    historical_data.to_csv(FILE_NAME)

    print(f"Data saved to {FILE_NAME}")
    return historical_data