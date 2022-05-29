from rest_framework import serializers
from .models import (
    Blog,
    Post,
)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
