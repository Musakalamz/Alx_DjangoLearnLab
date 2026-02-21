from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, PostSerializer


class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    ]
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    ]
    pagination_class = DefaultPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        followed_users = user.following.all()
        queryset = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        paginator = DefaultPagination()
        page = paginator.paginate_queryset(queryset, request, view=self)
        serializer = PostSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
