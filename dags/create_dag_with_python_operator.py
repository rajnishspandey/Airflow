from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'rajnish',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

# first version
# def greet(name, age):
#     print(f'Hello, World! I am {name}, my age is {age}')

# second version
# def greet(age, ti):
#     name = ti.xcom_pull(task_ids='getName')
#     print(f'Hello, World! I am {name}, my age is {age}')

# forth version
def greet(ti):
    first_name = ti.xcom_pull(task_ids='getName', key='first_name')
    last_name = ti.xcom_pull(task_ids='getName', key='last_name')
    age = ti.xcom_pull(task_ids='getAge', key='age')
    print(f'Hello, World! I am {first_name} {last_name}, and my age is {age}')

# third version
# def get_name():
#     return 'Rajnish'

def get_name(ti):
    ti.xcom_push(key='first_name', value='Rajnish')
    ti.xcom_push(key='last_name', value='Pandey')

# version 4
def get_age(ti):
    ti.xcom_push(key='age', value='30')

with DAG(default_args=default_args,
         dag_id = 'dag_with_python_operator_v06',
         description='this is our first dag with python operator',
         start_date=datetime(2024, 10, 3),
         schedule_interval='@daily'
         ) as dag:
    
    task1 = PythonOperator(
        task_id = 'greet',
        python_callable=greet,
        # op_kwargs={'age':20} #commented for version 4
    )

    task2 = PythonOperator(
        task_id='getName',
        python_callable=get_name
    )
    # added for version 4
    task3 = PythonOperator(
        task_id='getAge',
        python_callable=get_age
    )

    # task1
    [task2, task3] >> task1