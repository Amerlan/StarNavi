from posts.services import like_post


def test_post_creation_api(api_client, access_token):
    data = {
        'content': 'some text content',
    }
    api_client.credentials(HTTP_AUTHORIZATION='JWT ' + access_token)
    response = api_client.post('/api/posts/', data=data, format='json')
    assert response.status_code == 201


def test_post_like(api_client, create_post, access_token, create_test_user):
    assert create_post.likes.count() == 0
    url = f"/api/posts/{create_post.id}/like/"
    api_client.credentials(HTTP_AUTHORIZATION='JWT ' + access_token)
    response = api_client.post(url, format='json')
    assert response.status_code == 200
    assert create_post.likes.count() == 1
    assert create_test_user in create_post.likes.all()


def test_post_unlike(api_client, create_post, access_token, create_test_user):
    like_post(post=create_post, user=create_test_user)
    assert create_test_user in create_post.likes.all()
    url = f"/api/posts/{create_post.id}/unlike/"
    api_client.credentials(HTTP_AUTHORIZATION='JWT ' + access_token)
    response = api_client.post(url, format='json')
    assert response.status_code == 200
    assert create_post.likes.count() == 0
    assert create_test_user not in create_post.likes.all()
