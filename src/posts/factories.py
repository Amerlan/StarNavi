import factory
import faker
from datetime import date, timedelta
from factory.django import DjangoModelFactory
from .models import Post, PostLike
from users.models import User


faker = faker.Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('word')


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    content = factory.Faker('word')
    created_by = UserFactory()


class PostLikeFactory(DjangoModelFactory):
    class Meta:
        model = PostLike

    user = UserFactory()
    post = PostFactory()

    @classmethod
    def create(cls, **kwargs):
        instance = super().create(**kwargs)

        random_date = faker.date_time_between(
            start_date=date.today() - timedelta(days=30),
            end_date=date.today()
        )
        instance.like_date = random_date
        instance.save()
        return instance
