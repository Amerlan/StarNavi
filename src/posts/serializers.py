from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content',)

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        post = Post(created_by=user, **validated_data)
        post.save()
        return post


class AnalyticsSerializer(serializers.Serializer):
    like_date = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    def get_like_date(self, obj):
        return f"{obj['like_date'].astimezone()}".split('.')[0]
