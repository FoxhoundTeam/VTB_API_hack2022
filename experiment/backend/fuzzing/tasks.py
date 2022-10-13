from time import sleep
from celery import shared_task

@shared_task()
def do_fuzzing(apis):
    for api in apis:
        sleep(20)
    return