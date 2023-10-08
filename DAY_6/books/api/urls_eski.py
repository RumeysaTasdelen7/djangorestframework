from django.urls import path
from . import functional_views

urlpatterns = [
    path("hello/", functional_views.hello_rest_api, name="hello_api"),
    path("books/", functional_views.list_and_create_api_view, name="list_and_create_api"),
    path("books/<int:pk>/", functional_views.book_detail_api_view, name="book_detail_api_view"),
    path("authors/", functional_views.author_list, name="author_list"),
    path("authors/<int:pk>/", functional_views.author_detail_api_view, name="author_detail_api_view"),
]