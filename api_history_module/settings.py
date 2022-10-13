from pydantic import BaseModel
from celery.schedules import crontab


class Config(BaseModel):
    class CelerySettings:
        app_name: str = 'api_call_task'
        broker: str = 'pyamqp://guest@localhost//'
        main_function_name: str = 'call_api'
        # set schedule for api calling (every * seconds)
        schedule_settings: float = 30.0
        # set schedule for api calling (every day at * hour and * minutes)
        # schedule_settings: crontab = crontab(hour=0, minute=0)

    class DbSettings:
        host: str = 'localhost'
        port: int = 27017
        db_name: str = 'VtbApiHack'
        db_history_collection: str = 'api_requests_history'
        db_api_collection: str = 'api_collection'

    class ApiSettings:
        api_base_url: str = 'https://reqres.in/api/'
