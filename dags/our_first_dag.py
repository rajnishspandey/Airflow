from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'rajnish',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(dag_id='first_dag_v3',
         default_args=default_args,
         description='This is my first dag',
         start_date=datetime(2024, 9, 1),  # Start date should be in the past
         schedule_interval='@daily'
         ) as dag:

    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo this is the first task'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo Hey, this is the second task after 1'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo Hey, I am third task this will run with second task after 1'
    )    

    # Use >> for task dependency
    task1 >> task2
    task1 >> task3
