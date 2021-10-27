
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
import os

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization

default_args = {
    'owner': 'Octavio',
    'depends_on_past': False,
    'email': ['octadelsueldo@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    'sla': timedelta(hours=2)
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
with DAG(
    'scrapper',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='@daily',
    start_date=datetime(2021, 10, 24),
    catchup=False,
    tags=['scrapper'],
) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
 
    
    t1 = BashOperator(
            task_id='spider_star',
            bash_command="cd /opt/airflow/dags/web_scrap;scrapy crawl quotes",
        )

    t1.doc_md = dedent(
        """\
    #### Task Documentation
    My task scrap the website information and save it in a database using scrapy API

    """
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG
    dag.doc_md = """
    This is a documentation placed anywhere
    """  # otherwise, type it like this
    t1 