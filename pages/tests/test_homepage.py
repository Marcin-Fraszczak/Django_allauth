from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains


def test_url_exists_at_correct_location(client):
	response = client.get("/")
	assert response.status_code == 200
	response = client.get(reverse('pages:home'))
	assert response.status_code == 200
	assertContains(response=response, text="Welcome", status_code=200)

def test_correct_template_loaded(client):
	response = client.get(reverse('pages:home'))
	assert 'pages/home.html' in (t.name for t in response.templates)
	assertTemplateUsed('pages/home.html')