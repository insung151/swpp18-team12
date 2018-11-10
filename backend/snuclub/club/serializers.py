from django.utils import timezone
from rest_framework import serializers

from club.models import Club


class ClubSearchSerializer(serializers.ModelSerializer):
    overall = serializers.SerializerMethodField()
    now_recruiting = serializers.SerializerMethodField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Club
        fields = [
            'name', 'activity_type', 'profile_image', 'tags', 'category',
            'subcategory', 'overall', 'overall', 'now_recruiting',
        ]

    def get_overall(self, obj):
        if obj.user_rating_count > 0:
            return round(obj.clubrating.overall_sum / obj.user_rating_count, 2)
        else:
            return 0

    def get_now_recruiting(self, obj):
        if obj.clubdetail.join_due_datetime:
            return timezone.now() < obj.clubdetail.join_due_datetime
        else:
            return False
