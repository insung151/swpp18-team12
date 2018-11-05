from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class ActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, username, timestamp):
        return (
            six.text_type(username) + six.text_type(timestamp) + six.text_type("account")
        )


class ForgotPasswordTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, username, timestamp):
        return (
            six.text_type(username) + six.text_type(timestamp) + six.text_type("password")
        )


account_activation_token = ActivationTokenGenerator()
password_forgot_token = ForgotPasswordTokenGenerator()