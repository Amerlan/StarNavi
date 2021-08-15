from rest_framework.test import APIClient
from pytest import fixture
from users.models import User


@fixture
def api_client():
    return APIClient()


@fixture
def create_test_user(db):
    user = User.objects.create(username='test_user')
    user.set_password('password')
    user.save()
    return user


@fixture
def access_token(api_client, create_test_user):
    data = {
        'username': create_test_user.username,
        'password': 'password'
    }
    response = api_client.post('/api/users/login/', data=data, format='json')
    response_data = response.json()
    return response_data['access']
