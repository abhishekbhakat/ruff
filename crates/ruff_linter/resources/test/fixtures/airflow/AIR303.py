from airflow.operators.python import PythonOperator

# Invalid: using deprecated parameter
task1 = PythonOperator(
    task_id="my_task",
    task_concurrency=2
)

# Valid: using new parameter name
task2 = PythonOperator(
    task_id="my_task",
    max_active_tis_per_dag=2
)

# No concurrency parameter
task3 = PythonOperator(
    task_id="my_task"
)
