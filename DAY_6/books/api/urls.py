from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookListAndCreateApiView.as_view(), name="list_and_create_api_view"),
    path("books/<int:pk>/", views.BookDetailApiView.as_view(), name="book_detail_api_view"),
    #path("authors/", functional_views.list_and_create_api_view, name="list_and_create_api_view"),
    #path("authors/<int:pk>/", functional_views.author_detail_api_view, name="author_detail_api_view"),
]
