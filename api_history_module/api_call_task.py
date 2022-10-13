from celery import Celery
from pymongo import MongoClient
from datetime import datetime
from settings import settings
import requests
import mongo_worker

app = Celery("api_call_task", broker=settings.broker_uri)
app.conf.beat_schedule = {
    'main-task': {
        'task': 'api_call_task.call_api',
        'schedule': settings.crontab,
    },
}

AVAILABLE_METHODS = {
    "post",
    "get",
    "put",
    "patch",
    "delete",
}


# ToDo error handling and custom exceptions
@app.task
def call_api():
    client = MongoClient(settings.mongodb_server)
    db = client[settings.mongodb_db]
    history_collection = db[settings.db_history_collection]
    api_collection = db[settings.db_api_collection]
    api_endpoints = mongo_worker.do_find(api_collection, {"need_request": {"$eq": True}})

    for endpoint in api_endpoints:
        if not 'data' in endpoint:
            endpoint['data'] = None
        method = endpoint["method"].lower()
        if method in AVAILABLE_METHODS:
            response = requests.request(method, endpoint['url'], endpoint['data'])
            mongo_document = {
                'timestamp': datetime.now(),
                'url': endpoint['url'],
                'status': response.status_code,
                'response': response.text,
                'page': endpoint["_id"],
            }
            mongo_worker.do_insert(history_collection, mongo_document)

    return True
