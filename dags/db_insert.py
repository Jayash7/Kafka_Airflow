from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime
from src.Database.db_instance import pg_database

# Define DAG arguments
db_instance = pg_database()


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 12),
    'retries': 1,
}

# Define your DAG
dag = DAG(
    'insert_into_postgres',
    default_args=default_args,
    schedule_interval='@hourly',
)

# Define the SQL query to insert data into your PostgreSQL table
insert_sql = """
INSERT INTO test (id)
VALUES (%s)
"""
#value1 = {'value': 10}
value1 = 4000

# Define the task to execute the SQL query
insert_task = PostgresOperator(
    task_id='insert_into_postgres_task',
    postgres_conn_id='my_connection',  # This should match your Postgres connection ID in Airflow
    sql=insert_sql,
    #sql=db_instance.instance(insert_sql),
    parameters=[value1],  # Define your values here
    dag=dag,
)

# Define your task dependencies
insert_task
