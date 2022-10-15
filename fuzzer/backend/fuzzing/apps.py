from django.apps import AppConfig


class FuzzingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fuzzing'
