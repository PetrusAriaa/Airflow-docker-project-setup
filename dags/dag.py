import pendulum
from datetime import datetime, timedelta
from airflow.decorators import task, dag
from stock_trend.start_stock_trend import Start

local_tz = pendulum.timezone('Asia/Jakarta')


@dag(
    dag_id='rekdat-aria',
    schedule_interval='15 23 * * 5', # Set the schedule interval as needed
    start_date=datetime(2022, 11, 19, 19, 30, tzinfo=local_tz),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
)

def start_dag():
    
    @task
    def _start():
        Start()
        
    _start()

dag = start_dag()