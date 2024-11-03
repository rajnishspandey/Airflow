This Repository contains the details of Airflow with BashOperator, PythonOperator, Airflow with API

# [Buy me a coffee](https://rajnishspandey.gumroad.com/coffee)

# Commands are as follows.

Download Docker for mac OS and check in terminal if its installed correctly  using below commands
### 1 - docker --version
### 2 - docker-compose --version

###  1-	create docker-compose.yaml file using below command
>   curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'

## 2-	Remove below from the file
>   AIRFLOW__CORE__EXECUTOR : CeleryExecutor

### and make it Local
>   AIRFLOW__CORE__EXECUTOR: LocalExecutor

### depends_on, redis, airflow-worker, flower

### 3 -	Create folders using below commands
>   mkdir -p ./dags ./logs ./plugins ./config

### 4 -	Initialize the database
>   docker-compose up airflow-init
### 5 -	To launch the docker 
>   docker-compose up -d

### 6 -	to shutdown docker-compose
>   docker-compose down 

### 7 -	to shutdown and delete all the dags
>   docker-compose down -v

### 8 -	change the value
##### before
>   AIRFLOW__CORE__LOAD_EXAMPLES: ‘true’

#### After
>   AIRFLOW__CORE__LOAD_EXAMPLES: 'false'

### 9 -	restart 
>   docker-compose up airflow-init

>   docker-compose up -d

### 10 -	create virtual env and activate it
>   install apache airflow 

>   pip install apache-airflow

### 11 -	to check if docker is running 
>   docker ps

" 12 -	can we pass parameters from one task to another ?
yes , using xcom we can do it. "

Note:- Even if we can pass the value/share data between tasks through xcom - but the max size is 48kb

## cron job - Schedules 
![image](https://github.com/user-attachments/assets/f5189543-969a-439c-b04e-13f6f24fec3a)

## created custom cron job schedule 
[https://crontab.guru/]

# [Buy me a coffee](https://rajnishspandey.gumroad.com/coffee)
