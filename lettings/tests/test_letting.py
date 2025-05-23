import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.fixture
def sample_lettings():
    address = Address.objects.create(number=26, street="Rue", city="Ville", state="Provence", zip_code=1234, country_iso_code="+33")
    letting = Letting.objects.create(title="Test Letting", address=address)
    return letting


@pytest.mark.django_db
def test_lettings_index(client, sample_lettings):  #, create_lettings):
    response = client.get(reverse('lettings:lettings_index'))
    assert response.status_code == 200
    assert sample_lettings.title in str(response.content)  # .decode("utf-8")
