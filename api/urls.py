from rest_framework import routers
from django.urls import path, include
from .views import (
    BlogViewSet,
    PostViewSet,
)

router = routers.DefaultRouter()

router.register(r'blog', BlogViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
