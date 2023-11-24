import os
import csv
import datetime as dt
import pandas as pd
from apify_client import ApifyClient

def ExtractTrends():

    client = ApifyClient(os.getenv('APIFY_TOKEN'))

    timeRanges = ["today 1-m", "now 7-d"]
    
    for idx, t_range in enumerate(timeRanges):
        run_input = {
        "searchTerms": ["Blackpink"],
        "timeRange": t_range,
        "viewedFrom": "",
        "outputAsISODate": True,
        "csvOutput": True,
        }
        run = client.actor("emastra/google-trends-scraper").call(run_input=run_input)
        FILE_NAME = f"frames/{dt.datetime.now().strftime('%Y-%m-%d_search-trend')}_{idx}.csv"
        
        with open(FILE_NAME, mode='w', newline='') as csv_file:
            fieldnames = ['date', 'Blackpink']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()
            for item in client.dataset(run["defaultDatasetId"]).iterate_items():
                writer.writerow(item)
    
    # some transformation to merge ingested raw data
    df0 = pd.read_csv(f"frames/{dt.datetime.now().strftime('%Y-%m-%d_search-trend')}_0.csv")
    df1 = pd.read_csv(f"frames/{dt.datetime.now().strftime('%Y-%m-%d_search-trend')}_1.csv")
    
    df0['date'] = pd.to_datetime(df0['date']) \
                    .dt.tz_convert("Asia/Jakarta") \
                    .dt.strftime('%Y-%m-%d')

    df1['date'] = pd.to_datetime(df1['date']) \
                    .dt.tz_convert("Asia/Jakarta") \
                    .dt.strftime('%Y-%m-%d')
    df1 = df1.groupby(['date']).mean().astype('int8').reset_index()
    
    merged_df = df0.set_index('date').combine_first(df1.set_index('date')).reset_index()
    
    FILE_NAME = f"frames/{dt.datetime.now().strftime('%Y-%m-%d_search-trend')}.csv"
    
    merged_df.to_csv(FILE_NAME, index=False)
    os.remove(f"frames/{dt.datetime.now().strftime('%Y-%m-%d_search-trend')}_0.csv")
    os.remove(f"frames/{dt.datetime.now().strftime('%Y-%m-%d_search-trend')}_1.csv")
    print(f"file saved to {FILE_NAME}")
    return merged_df