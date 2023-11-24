import os
import subprocess
import datetime as dt

from sqlalchemy import create_engine

def Load(transformed_df):
    
    # update snapshot
    output = f"{dt.datetime.now().strftime('%Y-%m-%d_join')}.csv"
    transformed_df.to_csv(f"frames/{output}", index=False)
    bash = f""" curl -X PUT \
            -u {os.getenv('SIMPAN_UGM_USER')}:{os.getenv('SIMPAN_UGM_PASSWORD')} \
            "{os.getenv('SIMPAN_UGM_RECORDS_ENDPOINT')}/{dt.datetime.now().strftime("%Y-%m-%d_join")}.csv" \
            --data-binary @"frames/{dt.datetime.now().strftime('%Y-%m-%d_join')}.csv"
    """
    subprocess.call(bash, shell=True)
    print("Snapshot created")
    
    print("Loading to PostgreSQL database...")
    engine = create_engine(os.getenv('PG_CONNECTION'))
    transformed_df.to_sql('stock_trend', engine, index=False, if_exists='replace')
    print("Loading success.")