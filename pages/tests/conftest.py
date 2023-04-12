import pytest
from django.contrib.auth import get_user_model
from django.test import Client

email = 'a@a.pl'

@pytest.fixture
def client():
	return Client()

def user():
	user = get_user_model()(email=email)
	user.save()
	return user