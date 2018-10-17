from django.db import models


class IntegerRangeField(models.IntegerField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        super(IntegerRangeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)
