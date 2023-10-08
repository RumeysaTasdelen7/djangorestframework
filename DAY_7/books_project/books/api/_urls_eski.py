from django.urls import path
from . import views_functional

urlpatterns = [
    path("hello/", views_functional.hello_rest_api, name="hello_api"),
    path("books/", views_functional.list_and_create_api_view, name="list_and_create_api"),
    path("books/<int:pk>/", views_functional.book_detail_api_view, name="book_detail_api_view"),
    path("authors/", views_functional.author_list, name="author_list"),
    path("authors/<int:pk>/", views_functional.author_detail_api_view, name="author_detail_api_view"),
]