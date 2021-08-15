from django.db.models import QuerySet, Count
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError as ValidationErrorException
from rest_framework.exceptions import ValidationError
from .models import Post, PostLike


def filter_by_period(*, queryset: QuerySet, from_date: str = None, to_date: str = None):
    try:
        if all([from_date, to_date]):
            queryset = queryset.filter(like_date__range=(from_date, to_date))
        elif from_date is not None:
            queryset = queryset.filter(like_date__gte=from_date)
        elif to_date is not None:
            queryset = queryset.filter(like_date__lte=from_date)
    except ValidationErrorException:
        raise ValidationError("Invalid date format")
    return queryset



def get_post(*, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post


def likes_analysis(*, from_date: str, to_date: str):
    posts = PostLike.objects.all()
    posts = filter_by_period(queryset=posts, from_date=from_date, to_date=to_date)
    queryset = posts.values('like_date').annotate(count=Count('like_date')).order_by('like_date')
    return queryset

