from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # to send signals for profile creation and save
    def ready(self):
        import users.signals
