from django.urls import path
from .views import PostCreateApi, PostLikeApi, PostUnlikeApi, AnalyticsApi


urlpatterns = [
    path('', PostCreateApi.as_view(), name='create'),
    path('analytics/', AnalyticsApi.as_view(), name='analytics'),
    path('<int:post_id>/like/', PostLikeApi.as_view(), name='like'),
    path('<int:post_id>/unlike/', PostUnlikeApi.as_view(), name='unlike'),
]
