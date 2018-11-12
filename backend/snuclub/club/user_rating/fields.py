from rest_framework import serializers


class ScoringField(serializers.IntegerField):

    def __init__(self, **kwargs):
        kwargs.update({'min_value': 1, 'max_value': 10})
        super(ScoringField, self).__init__(**kwargs)


class NonScoringField(serializers.IntegerField):

    def __init__(self, **kwargs):
        kwargs.update({'min_value': 1, 'max_value': 5})
        super(NonScoringField, self).__init__(**kwargs)
