from .models import Post
from users.models import User


def like_post(*, post: Post, user: User):
    post.likes.add(user)


def unlike_post(*, post: Post, user: User):
    post.likes.remove(user)
