from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from ..models import Author, Book
from .serializers_eski import BookSerializer, AuthorSerializer
from rest_framework.generics import ListAPIView


class BookListAndCreateApiView(APIView):
    def get(self, request):
        books = Book.objects.filter(activate=1)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookDetailApiView(APIView):
    def get_object(self, pk):
        book = get_object_or_404(Book, pk=pk)
        return book
    
    def get(self, request, pk):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_object(pk=pk)
        book.delete()
        return Response({
            "OK": {
                "code": f"{status.HTTP_204_NO_CONTENT}",
                "message": f"{book.name} kitabı silindi!"
            }
        })


class AuthorListCreateApiView(APIView):

    def get(self, request):
        authors = Author.objects.all()
        context = {'request': request}
        serializer = AuthorSerializer(authors, many=True , context=context)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AuthorDetailApiView(APIView):

    def get_object(self, pk):
        author = get_object_or_404(Author, pk=pk)
        return author

    def get(self, request, pk):
        author = self.get_object(pk=pk)
        serializer = AuthorSerializer(author, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        author = self.get_object(pk=pk)
        serializer = AuthorSerializer(instance=author, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_object(pk=pk)
        author.delete()
        return Response(
            {
                'OK': {
                    'code': f"{status.HTTP_204_NO_CONTENT}",
                    'message': "{} Silindi!".format(author.name)
                }
            }

        )