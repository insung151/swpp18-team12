import re
import json
from rest_framework import serializers
from club.models import Club, ClubDetail, Tag
from django.core.exceptions import ObjectDoesNotExist


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name',
                  'profile_image',
                  'activity_type',
                  'short_description',
                  'category',
                  'subcategory',
                  'tags',
                ]
    tags = TagSerializer(many=True, default=[])

    def validate_name(self, value):
        if Club.objects.filter(name=value).exists():
            raise serializers.ValidationError('Already exists')
        return value

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        club = Club(**validated_data)
        for tag in tags_data:
            try:
                add_tag = Tag.objects.get(name=tag.get('name'))
            except ObjectDoesNotExist:
                add_tag = Tag(**tag)
                add_tag.save()
            club.save()
            club.tags.add(add_tag)
        club.save()
        return club

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.activity_type = validated_data.get('activity_type', instance.activity_type)
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.save()
        return instance


class ClubDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubDetail
        fields = ['join_due_datetime',
                  'join_link',
                  'site_link',
                  'long_description',
                  'history']

    def update(self, instance, validated_data):
        instance.join_due_datetime = validated_data.get('join_due_datetime', instance.join_due_datetime)
        instance.join_link = validated_data('join_link', instance.join_link)
        instance.site_link = validated_data('site_link', instance.site_link)
        instance.long_description = validated_data('long_description', instance.long_description)
        instance.history = validated_data('history', instance.history)
        instance.save()
        return instance


class ChangeProfileImageSerializer(serializers.Serializer):
    profile_image = serializers.ImageField(allow_null=True)


class ChangeAdminSerializer(serializers.Serializer):
    admin = serializers.CharField()