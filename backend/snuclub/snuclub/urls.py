"""snuclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='SNUCLUB API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls'), name='accounts'),
    path('api/club/', include('club.urls'), name='club'),
<<<<<<< HEAD
    path('api/rating/', include('club.user_rating.urls'), name='user_rating'),
=======
>>>>>>> 7a95522... Add club urls
]

if hasattr(settings, 'ENV_SETTINGS_MODE') and settings.ENV_SETTINGS_MODE == 'dev':
    urlpatterns = [path('', schema_view)] + urlpatterns
