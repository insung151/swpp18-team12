from django.urls import path, include
from rest_framework import routers

from .views import UserRatingViewSet

router = routers.SimpleRouter()
router.register('', UserRatingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
