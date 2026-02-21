from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    FeedView,
    LikePostView,
    PostViewSet,
    UnlikePostView,
)


router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='post_like'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='post_unlike'),
]

urlpatterns += router.urls
