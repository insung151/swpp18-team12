from rest_framework import serializers

from club.models import Club
from club.user_rating.fields import ScoringField, NonScoringField
from club.user_rating.models import UserRating


class CurrentUserProfileDefault:
    def set_context(self, serializer_field):
        self.user_profile = serializer_field.context['request'].user.userprofile

    def __call__(self):
        return self.user_profile


class UserRatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserProfileDefault())
    club = serializers.PrimaryKeyRelatedField(
        queryset=Club.objects.all()
    )
    overall = ScoringField()
    operation = ScoringField()
    facility = ScoringField()
    newcomer = ScoringField()
    compulsory = NonScoringField()
    meetfreq = NonScoringField()
    age = NonScoringField()
    friendliness = NonScoringField()
    alcohol = NonScoringField()

    class Meta:
        model = UserRating
        fields = '__all__'


class UserRatingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRating
        fields = ('club', 'comments',)