from django.apps import AppConfig


class UserRatingConfig(AppConfig):
    name = 'club.user_rating'

    def ready(self):
        from . import signals
