from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthororReadOnly, IsSuperuser

# Create your views here.


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


#***************VIEWSETS********************

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthororReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer 


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer