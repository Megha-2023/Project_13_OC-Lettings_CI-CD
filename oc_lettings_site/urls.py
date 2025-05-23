from django.contrib import admin
from django.urls import path, include
from  .views import index
import profiles.views


urlpatterns = [
    path('', index, name='index'),
    path('lettings/', include('lettings.urls'), name='lettings_index'),
    path('profiles/', include('profiles.urls'), name='profiles_index'),
    # path('lettings/', lettings.views.lettings_index, name='lettings_index'),
    # path('lettings/<int:letting_id>/', lettings.views.letting, name='letting'),
    # path('profiles/', profiles.views.profiles_index, name='profiles_index'),
    # path('profiles/<str:username>/', profiles.views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
