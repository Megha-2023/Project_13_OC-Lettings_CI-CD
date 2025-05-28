import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.fixture(name="sample")  # to remove redefined-outer-name pylint error
def sample_lettings():
    address = Address.objects.create(
        number=26,
        street="Rue",
        city="Ville",
        state="Provence",
        zip_code=1234,
        country_iso_code="+33"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    return letting


@pytest.mark.django_db
def test_lettings_index(client, sample):
    response = client.get(reverse('lettings:lettings_index'))
    assert response.status_code == 200
    assert sample.title in str(response.content)


@pytest.mark.django_db
def test_letting_with_id(client, sample):
    response = client.get(reverse('lettings:letting', kwargs={'letting_id': sample.id}))
    assert response.status_code == 200
    assert sample.title in str(response.content)
