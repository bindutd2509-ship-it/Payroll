from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    name = 'app.companies'

    def ready(self):
        import app.companies.signals
