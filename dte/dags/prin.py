from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import psycopg2

def extract_and_load_weather_data():
    conn = psycopg2.connect(
        dbname='data-engineer-database',
        user='gabrielpin25_coderhouse',
        password='00b99Uzw8s',
        host='data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com',
        port='5439'
    )

    query = "SELECT * FROM weather_data LIMIT 100;"

    df = pd.read_sql_query(query, conn)

    df.to_csv('/usr/local/airflow/dags/weather_data_sample.csv', index=False)

    conn.close()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_data_dag',
    default_args=default_args,
    description='DAG para extraer y cargar datos de clima diariamente en Redshift',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

extract_load_task = PythonOperator(
    task_id='extract_and_load_weather_data',
    python_callable=extract_and_load_weather_data,
    dag=dag,
)
