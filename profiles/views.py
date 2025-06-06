""" Module contains views for Profiles"""

from django.shortcuts import render
from .models import Profile


# Create your views here.
# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis
# dictum lacus d


def profiles_index(request):
    """ Function to display all profiles"""

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et
# males


def profile(request, username):
    """ Function to display single profile"""

    profile_obj = Profile.objects.get(user__username=username)
    context = {'profile': profile_obj}
    return render(request, 'profile.html', context)
