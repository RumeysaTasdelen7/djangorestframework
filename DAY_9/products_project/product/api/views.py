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

class RetrieveUpdateDestroyCategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ListCreateProductAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]

class RetrieveUpdateDestroyProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ListProductOfCategory(generics.ListAPIView):
    serializer_class = ProductOfCategorySerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Product.objects.filter(category_id=pk)
    

class ListCommentOfProduct(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comment.objects.filter(product_id=pk)
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, id=pk)
        user = self.request.user

        serializer.save(user=user, product=product)
