import re
import json
from rest_framework import serializers
from club.models import Club, ClubDetail, Tag, ClubRating
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

    def create(self, validated_data):
        if Club.objects.filter(name=validated_data.get('name')).exists():
            raise serializers.ValidationError('Already exists')
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
        club_detail = ClubDetail(club=club)
        club_detail.save()
        club_rating = ClubRating(club=club)
        club_rating.save()
        return club

    def update(self, instance, validated_data):
        if instance.name != validated_data.get('name'):
            if Club.objects.filter(name=validated_data.get('name')).exists():
                raise serializers.ValidationError('Already exists')
            else:
                instance.name = validated_data.get('name', instance.name)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.activity_type = validated_data.get('activity_type', instance.activity_type)
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.tags.clear()
        tags_data = validated_data.get('tags')
        for tag in tags_data:
            try:
                add_tag = Tag.objects.get(name=tag.get('name'))
            except ObjectDoesNotExist:
                add_tag = Tag(**tag)
                add_tag.save()
            instance.tags.add(add_tag)
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


class ChangeProfileImageSerializer(serializers.Serializer):
    profile_image = serializers.ImageField(allow_null=True)


class ChangeAdminSerializer(serializers.Serializer):
    admin = serializers.CharField()