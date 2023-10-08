from rest_framework import generics, mixins, permissions
from ..models import Category, Product, Comment
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .serializers import CategorySerializer, ProductSerializer, ProductOfCategorySerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


def index(request):
    return JsonResponse({"message": "Hello World"})

class ListCreateCategoryAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]


