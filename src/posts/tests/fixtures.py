from pytest import fixture
from posts.models import Post


@fixture
def create_post(db, create_test_user):
    post = Post.objects.create(created_by=create_test_user)
    return post
