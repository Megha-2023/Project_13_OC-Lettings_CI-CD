from django.contrib import admin
from django.urls import path, include, get_resolver
from django.http import HttpResponse
from .views import index, trigger_error


urlpatterns = [
    path('', index),
    path('lettings/', include('lettings.urls'), name='lettings_index'),
    path('profiles/', include('profiles.urls'), name='profiles_index'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
