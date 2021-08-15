from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password1 = serializers.CharField(max_length=25)
    password2 = serializers.CharField(max_length=25)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords are not the same')
        data.pop('password2')
        data['password'] = data.pop('password1')
        return data

    def create(self, validated_data):
        try:
            user = User(username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
        except IntegrityError:
            raise ValidationError('Username is taken.')
        return user


class UserActivitySerializer(serializers.Serializer):
    last_login = serializers.SerializerMethodField()
    last_request = serializers.SerializerMethodField()

    def get_last_login(self, obj):
        return f"{obj.last_login.astimezone()}".split('.')[0]

    def get_last_request(self, obj):
        return f"{obj.last_request.astimezone()}".split('.')[0]
