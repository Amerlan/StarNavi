from django.urls import path, include
from .yasg import urlpatterns as swagger_urlpatterns

api_urlpatterns = [
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
]

urlpatterns = [
    path('api/', include((api_urlpatterns, 'api'))),
]

urlpatterns += swagger_urlpatterns

