import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.fixture(name="sample")
def sample_profile():
    user_obj = User.objects.create(
        username="AirWow",
        first_name="Ada",
        last_name="Paul"
    )
    profile = Profile.objects.create(user=user_obj,
                                     favorite_city="Grenoble")
    return profile


@pytest.mark.django_db
def test_profiles_index(client):
    response = client.get(reverse('profiles:profiles_index'))
    assert response.status_code == 200
    assert 'Profiles' in str(response.content)


@pytest.mark.django_db
def test_profile_with_id(client, sample):
    response = client.get(reverse('profiles:profile', kwargs={'username': sample.user}))
    assert response.status_code == 200
    assert sample.user.username in str(response.content)
