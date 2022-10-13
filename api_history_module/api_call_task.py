from celery import Celery
from pymongo import MongoClient
from datetime import datetime
from settings import Config
import api_sender
import mongo_worker

app = Celery(Config.CelerySettings.app_name, broker=Config.CelerySettings.broker)
app.conf.beat_schedule = {
    'main-task': {
        'task': f'{Config.CelerySettings.app_name}.{Config.CelerySettings.main_function_name}',
        'schedule': Config.CelerySettings.schedule_settings,
    },
}

client = MongoClient(Config.DbSettings.host, Config.DbSettings.port)
db = client[Config.DbSettings.db_name]
history_collection = db[Config.DbSettings.db_history_collection]
api_collection = db[Config.DbSettings.db_api_collection]


# ToDo error handling and custom exceptions
@app.task
def call_api():
    api_endpoints = mongo_worker.do_find(api_collection)

    for endpoint in api_endpoints:
        if not 'data' in endpoint:
            endpoint['data'] = None
        request = None
        if endpoint['method'] == 'post':
            request = api_sender.post_request(
                Config.ApiSettings.api_base_url + endpoint['url'],
                endpoint['data']
            )
        elif endpoint['method'] == 'get':
            request = api_sender.get_request(
                Config.ApiSettings.api_base_url + endpoint['url'],
                endpoint['data']
            )

        elif endpoint['method'] == 'put':
            request = api_sender.put_request(
                Config.ApiSettings.api_base_url + endpoint['url'],
                endpoint['data']
            )

        elif endpoint['method'] == 'patch':
            request = api_sender.patch_request(
                Config.ApiSettings.api_base_url + endpoint['url'],
                endpoint['data']
            )

        elif endpoint['method'] == 'delete':
            request = api_sender.delete_request(
                Config.ApiSettings.api_base_url + endpoint['url'],
                endpoint['data']
            )

        if request:
            mongo_document = {
                'timestamp': datetime.now(),
                'url': endpoint['url'],
                'status': request.status_code,
                'response': request.text
            }
            mongo_worker.do_insert(history_collection, mongo_document)

    return True
