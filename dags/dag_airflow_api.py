from datetime import datetime, timedelta
from airflow.decorators import dag, task


default_arg = {
    'owner':'Rajnish',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

@dag(default_args=default_arg, 
     dag_id='dag_with_airflow_api_v01', 
     description='This is a dag with airflow api',
     schedule_interval='@daily',
     start_date=datetime(2024, 10, 3))
def hello_world_etl():
    @task()
    def get_name():
        return 'Rajnish'
    
    @task()
    def get_age():
        return 30

    @task()
    def greet(name, age):
        print(f'I am {name} and my Age is {age}')


    name = get_name()
    age = get_age()
    greet(name=name, age=age)


greet_dag = hello_world_etl()