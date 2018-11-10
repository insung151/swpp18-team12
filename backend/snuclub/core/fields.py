from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class IntegerRangeField(models.IntegerField):
    def __init__(self, min_value=None, max_value=None, validators=[], *args, **kwargs):
        self.min_value = min_value
        self.max_value = max_value
        validators += [
            MinValueValidator(min_value),
            MaxValueValidator(max_value)
        ]
        super(IntegerRangeField, self).__init__(validators=validators, *args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

