from post.viewsets import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post', PostViewSet, basename='post')
