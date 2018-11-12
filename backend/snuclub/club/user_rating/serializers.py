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
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = UserRating
        fields = '__all__'

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user and \
            request.user.is_authenticated and \
            obj.user.user == request.user


class UserRatingListSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = UserRating
        fields = ('club', 'comments', 'updated_at', 'is_owner')

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user and \
            request.user.is_authenticated and \
            obj.user.user == request.user
