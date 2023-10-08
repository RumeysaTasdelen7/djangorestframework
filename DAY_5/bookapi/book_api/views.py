from django.shortcuts import render
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)
    
#**********üsteki iki view birleşti************

@api_view(['GET', 'POST'])
def books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)



    
@api_view(['GET'])
def book_detail(request, id):
    try:
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except:
        return Response({'eroor': 'Eşleşen bir kayıt bulunamadı'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def book_update(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def book_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#**********üsteki üçview birleşti************


@api_view(['GET', 'PUT', 'DELETE'])
def book_change(request, id):
    try:
        book = Book.objects.get(pk=id)
        
    except:
        return Response({'eroor': 'Eşleşen bir kayıt bulunamadı'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    