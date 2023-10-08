from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.filter(activate=True)
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()
    
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    

class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer