from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from books.models import Book

# Create your views here.

class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer