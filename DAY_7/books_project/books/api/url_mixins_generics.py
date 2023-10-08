from django.urls import path
# from . import views_classAPi
from . import views

# urlpatterns = [
#     path('books/', views_classAPi.BookListAndCreateApiView.as_view(), name='book_list_and_create'),
#     path('books/<int:pk>/', views_classAPi.BookDetailApiView.as_view(), name='book_detail'),
#     path('authors/', views_classAPi.AuthorListCreateApiView.as_view(), name='author_list_and_create'),
#     path('authors/<int:pk>/', views_classAPi.AuthorDetailApiView.as_view(), name='author_detail'),
# ]


urlpatterns = [
    path('books/', views.BookListCreateAPIView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailAPIView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListCreateAPIView.as_view(), name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailAPIView.as_view(), name='author_detail'),
]