from django.urls import path
from .views import SignUpApi, UserActivityApi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', SignUpApi.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('activity/', UserActivityApi.as_view(), name='activity'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
