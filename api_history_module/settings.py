from typing import Any, Optional
from pydantic import BaseSettings, validator, AmqpDsn
from celery.schedules import crontab


class Config(BaseSettings):
    rmq_host: str = 'localhost'
    rmq_user: str = "guest"
    rmq_pass: Optional[str] = None
    rmq_port: str = "5672"
    
    schedule_minute: Optional[str] = None
    schedule_hour: Optional[str] = "0"
    schedule_day_of_week: Optional[str] = None
    schedule_day_of_month: Optional[str] = None
    schedule_month_of_year: Optional[str] = None

    mongodb_server: str = 'localhost'
    mongodb_db: str = "api"
    db_history_collection: str = 'api_requests_history'
    db_api_collection: str = 'api_collection'
    api_base_url: str = 'http://51.250.82.157'
    
    broker_uri: Optional[AmqpDsn] = None
    crontab: Optional[crontab]
    
    @validator("crontab", pre=True)
    def create_crontab(cls, v: Optional[crontab], values: dict[str, Any]) -> Any:
        if isinstance(v, crontab):
            return v
        schedule = dict(
            minute=values.get("schedule_minute"),
            hour=values.get("schedule_hour"),
            day_of_week=values.get("schedule_day_of_week"),
            day_of_month=values.get("schedule_day_of_month"),
            month_of_year=values.get("schedule_month_of_year"),
        )
        return crontab(**dict(filter(lambda s: s[1] is not None, schedule.items())))
    
    @validator("broker_uri", pre=True)
    def assemble_broker_connection(cls, v: Optional[str], values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return AmqpDsn.build(
            scheme="amqp",
            host=values.get("rmq_host"),
            user=values.get("rmq_user"),
            password=values.get("rmq_pass"),
            port=values.get("rmq_port"),
        )
        
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
settings = Config()
