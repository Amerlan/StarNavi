from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUpSerializer, UserActivitySerializer


class SignUpApi(APIView):
    permission_classes = (AllowAny, )

    @swagger_auto_schema(
        operation_description='User registration',
        request_body=SignUpSerializer
    )
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class UserActivityApi(APIView):
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(
        operation_description='User activity info'
    )
    def get(self, request):
        serializer = UserActivitySerializer(request.user)
        print(serializer.data)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
