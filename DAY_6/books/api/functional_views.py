from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from ..models import Author, Book
from .serializers_eski import BookSerializer, AuthorSerializer

@api_view()
def hello_rest_api(request):
    return Response({"message": "Hello Django Rest Framework"})

@api_view(("GET", "POST"))
def list_and_create_api_view(request):
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(("GET", "PUT", "DELETE"))
def book_detail_api_view(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        book.delete()
        return Response({
            "OK": {
                "code": f"{status.HTTP_204_NO_CONTENT}",
                "message": f"{book.name} kitabı silindi!"
            }
        })
    

@api_view(("GET", "POST"))
def author_list(request):
    if request.method == 'GET':
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(("GET", "PUT", "DELETE"))
def author_detail_api_view(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = AuthorSerializer(instance=author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        author.delete()
        return Response({
            "OK": {
                "code": f"{status.HTTP_204_NO_CONTENT}",
                "message": f"{author.name} yazarı silindi!"
            }
        })