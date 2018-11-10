from django.db.models import Q, Count
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from club.user_rating.models import UserRating
from club.user_rating.serializers import UserRatingListSerializer
from club.models import Club
from club.serializers import ClubSearchSerializer


def get_params_list(query_dict, key):
    item = query_dict.get(key, [])
    if item:
        return item.split(',')
    else:
        return []


class ClubUserRatingListView(ListAPIView):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingListSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return super(ClubUserRatingListView, self).get_queryset()\
            .filter(club_id=self.kwargs['pk'])


class ClubSearchAPIView(GenericAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSearchSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword', '')
        category = get_params_list(request.GET, 'cat')
        sub_cat = get_params_list(request.GET, 'sub')
        activity = get_params_list(request.GET, 'type')

        query = Q()
        if keyword:
            query = Q(name__contains=keyword) | Q(tags__name__contains=keyword)

        if category:
            query |= Q(category__in=category)

        if sub_cat:
            query |= Q(subcategory__in=sub_cat)

        if activity:
            query |= Q(activity_type__in=activity)

        queryset = self.get_queryset()\
            .select_related('clubrating', 'clubdetail',)\
            .filter(query).annotate(user_rating_count=Count('user_ratings'))\
            .prefetch_related('tags')
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
