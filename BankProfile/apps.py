from django.apps import AppConfig


class BankprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BankProfile'

    def ready(self):
        import BankProfile.signals