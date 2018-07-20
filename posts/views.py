# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import render
from posts.models import Post, Presentation, Main
from posts.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer, UserSerializer, PresentationSerializer, MainSerializer
from rest_framework import generics, permissions





class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
  
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class PresentationList(generics.ListCreateAPIView):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class MainList(generics.ListCreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


def application(request):
    return render(request, 'index.html', {})
