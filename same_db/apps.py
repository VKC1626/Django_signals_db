from django.apps import AppConfig


class SameDbConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "same_db"

    def ready(self):
        import same_db.signals
