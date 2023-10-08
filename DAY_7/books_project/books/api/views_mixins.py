from rest_framework import generics, status, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class ListModelMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class CreateModelMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RetrieveModelMixin:
    def retrieve(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
    
class UpdateModelMixin:
    def update(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(obj, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DestroyModelMixin:
    def destroy(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        obj.delete()
        return Response(
            {
                "OK": {
                    "code": f"{status.HTTP_204_NO_CONTENT}",
                    "message": f"{obj.name} silindi!"
                }
            }
        )
    


class BookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.filter(activate=True)
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class BookDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk, *args, **kwargs)
    
    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)
    
    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, pk, *args, **kwargs)
    

class AuthorListCreateAPIView(ListModelMixin, CreateModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class AuthorDetailAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk, *args, **kwargs)
    
    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)
    
    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, pk, *args, **kwargs)