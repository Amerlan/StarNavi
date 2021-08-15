def test_signup(api_client, db):
    data = {
        'username': 'admin',
        'password1': 'password',
        'password2': 'password',
    }
    response = api_client.post('/api/users/signup/', data=data, format='json')
    assert response.status_code == 201


def test_wrong_signup(api_client):
    data = {
        'username': 'admin',
        'password1': 'password',
        'password2': 'password1',
    }
    response = api_client.post('/api/users/signup/', data=data, format='json')
    assert response.status_code == 400


def test_user_login(api_client, create_test_user):
    data = {
        'username': 'test_user',
        'password': 'password'
    }
    response = api_client.post('/api/users/login/', data=data, format='json')
    assert response.status_code == 200


def test_user_wrong_login(api_client, create_test_user):
    data = {
        'username': 'wrong_username',
        'password': 'password'
    }
    response = api_client.post('/api/users/login/', data=data, format='json')
    assert response.status_code == 401
