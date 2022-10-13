# Модуль сбора истории API

### Что нужно для запуска
* RabbitMQ
* MongoDB

### Процесс запуска
1. Открыть консоль и ввести
```
poetry install
```
2. Настроить settings.py
3. Запустить Celery
```
Для Windows:
celery -A api_call_task beat
celery -A api_call_task worker --loglevel=INFO -P gevent

Для Unix:
celery -A api_call_task worker -B
```