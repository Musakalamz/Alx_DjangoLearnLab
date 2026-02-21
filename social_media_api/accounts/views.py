from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import (
    LoginSerializer,
    ProfileSerializer,
    RegisterSerializer,
    UserSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(pk=response.data['id'])
        token, created = Token.objects.get_or_create(user=user)
        data = {
            'user': UserSerializer(user).data,
            'token': token.key,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {
            'user': UserSerializer(user).data,
            'token': token.key,
        }
        return Response(data, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response(
                {'detail': 'You cannot follow yourself.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        request.user.following.add(target)
        return Response(
            {
                'detail': f'You are now following {target.username}.',
                'following_count': request.user.following.count(),
            },
            status=status.HTTP_200_OK,
        )


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response(
                {'detail': 'You cannot unfollow yourself.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        request.user.following.remove(target)
        return Response(
            {
                'detail': f'You have unfollowed {target.username}.',
                'following_count': request.user.following.count(),
            },
            status=status.HTTP_200_OK,
        )
