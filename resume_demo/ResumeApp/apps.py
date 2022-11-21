from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # app_name : ResumeApp
    # when the app is up and running (ResumeApp), signals is all working
    name = 'ResumeApp'

    # Way to connect the signal with the function:
    # Need to connect the signals file with the app.py file ready function in order to use them.
    def ready(self):
        import ResumeApp.signals