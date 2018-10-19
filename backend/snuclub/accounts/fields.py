from rest_framework import serializers


class PasswordField(serializers.CharField):
    def __init__(self, **kwargs):
        default = {
            'min_length': 8,
            'write_only': True,
            'required': True,
            'style': {'input_type': 'password'}
        }
        kwargs.update(default)
        super(PasswordField, self).__init__(**kwargs)
