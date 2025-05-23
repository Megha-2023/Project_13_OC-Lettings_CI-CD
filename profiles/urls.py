from django.urls import path
from .views import profiles_index, profile

app_name = 'profiles'

urlpatterns = [
    path('', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
]
