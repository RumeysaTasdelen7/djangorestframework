from rest_framework import generics, permissions

from .models import Post
from.serializers import PostSerializer
from .permissions import IsAuthororReadOnly, IsSuperUser


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
