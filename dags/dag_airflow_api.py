from datetime import datetime, timedelta
from airflow.decorators import dag, task


default_arg = {
    'owner':'Rajnish',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

@dag(default_args=default_arg, 
     dag_id='dag_with_airflow_api_v02', 
     description='This is a dag with airflow api',
     schedule_interval='@daily',
     start_date=datetime(2024, 10, 3))
def hello_world_etl():
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name':'Rajnish',
            'last_name':'Pandey'
        }
    
    @task()
    def get_age():
        return 29

    @task()
    def greet(first_name, last_name, age):
        print(f'I am {first_name} {last_name} and my Age is {age}')

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],
          last_name=name_dict['last_name'], 
          age=age)

greet_dag = hello_world_etl()