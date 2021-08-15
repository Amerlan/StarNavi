from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.services import update_request_time
from starnavi.swagger_params import from_date_params, to_date_params
from .serializers import PostSerializer, AnalyticsSerializer
from .services import like_post, unlike_post
from .selectors import get_post, likes_analysis


class PostCreateApi(APIView):
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        operation_description='Post creation',
        request_body=PostSerializer
    )
    def post(self, request):
        update_request_time(user=request.user)
        serializer = PostSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class PostLikeApi(APIView):
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        operation_description='Post like'
    )
    def post(self, request, post_id):
        update_request_time(user=request.user)
        post = get_post(post_id=post_id)
        like_post(post=post, user=request.user)
        return Response(status=status.HTTP_200_OK)


class PostUnlikeApi(APIView):
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        operation_description='Post unlike'
    )
    def post(self, request, post_id):
        update_request_time(user=request.user)
        post = get_post(post_id=post_id)
        unlike_post(post=post, user=request.user)
        return Response(status=status.HTTP_200_OK)


class AnalyticsApi(APIView):
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        operation_description='Analytics aggregated by date for period',
        manual_parameters=[
            from_date_params, to_date_params
        ]
    )
    def post(self, request):
        update_request_time(user=request.user)
        params = request.query_params
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)
        queryset = likes_analysis(from_date=from_date, to_date=to_date)
        serializer = AnalyticsSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
