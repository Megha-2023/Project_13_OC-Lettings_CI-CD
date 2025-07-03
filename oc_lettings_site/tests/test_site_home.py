import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_site_index_page(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert "Holiday Homes" in str(response.content)
