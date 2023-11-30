import subprocess
from dotenv import load_dotenv
from stock_trend.ingest_raw.ingest import StartIngest
from stock_trend.pipeline.etl import StartPipeline

def Start():
    load_dotenv('.env.production')
    StartIngest()
    StartPipeline()
    
    subprocess.call("rm -rf frames", shell=True)

Start()