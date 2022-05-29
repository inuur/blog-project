from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    Blog,
    Post
)
from .serializer import BlogSerializer, PostSerializer


class BlogViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    @action(methods=['get'], detail=True)
    def posts(self, request, pk=None):
        blog_posts = Post.objects.filter(blog_id=pk).all()
        posts_serializer = PostSerializer(data=blog_posts, many=True)
        posts_serializer.is_valid()
        return Response(posts_serializer.data)

    @action(methods=['post'], detail=True)
    def follow(self, request, pk=None):
        self.request.user.followed_blogs.add(
            Blog.objects.get(pk=pk)
        )
        return Response(status=status.HTTP_200_OK)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=['post'], detail=True)
    def read(self, request, pk=None):
        self.request.user.read_posts.add(
            Post.objects.get(pk=pk)
        )
        return Response(status=status.HTTP_200_OK)
