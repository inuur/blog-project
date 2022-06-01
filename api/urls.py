from rest_framework import routers
from django.urls import path, include
from .views import (
    BlogViewSet,
    PostViewSet,
    FeedView,
)

router = routers.DefaultRouter()

router.register(r'blog', BlogViewSet)
router.register(r'post', PostViewSet)
router.register(r'feed', FeedView, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
]
