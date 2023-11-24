import pendulum
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from stock_trend.start_stock_trend import Start

local_tz = pendulum.timezone('Asia/Jakarta')

# Define the default_args for your DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 19, 19, 30, tzinfo=local_tz),
    'retries': 1,
    'catchup': False,
    'retry_delay': timedelta(minutes=10),
}

# Define the DAG
dag = DAG(
    'my_spark_dag',
    default_args=default_args,
    description='A DAG to run a Spark job',
    schedule_interval='15 23 * * 5', # Set the schedule interval as needed
)

# Define the PythonOperator task
spark_task = PythonOperator(
    task_id='run_spark_script',
    python_callable=Start,
    dag=dag,
)