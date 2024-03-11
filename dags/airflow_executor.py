from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.airflow_test import testing

default_args= {
    'owner':'airflow',
    'start_date':datetime(2024,3,8),
    'retries':1
}

dag_id = 'my_dag_id'
dag = DAG(
    dag_id= dag_id,
    default_args = default_args,
    #schedule_interval = '@daily'
    schedule_interval = '*/2 * * * *'
)


start_test_exectutor = PythonOperator(
    task_id = 'test_1',
    python_callable = testing,
    dag =dag
)

start_test_exectutor