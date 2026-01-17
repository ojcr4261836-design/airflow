from airflow.sdk import DAG
import datetime
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

#dag info
with DAG(
    dag_id="example_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:
    run_this_last = EmptyOperator(
        task_id="run_this_last",
    )

#bash operate
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t22
    # branch 생성을 위한 주석 생성 
