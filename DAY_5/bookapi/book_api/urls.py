from django.urls import path
from . import views

urlpatterns = [
    #path('', views.book_list, name="list"),
    #path('create', views.book_create, name="create"),
    path("", views.books, name="books"),
    path('<int:id>/', views.book_change, name="change"),
    #path('<int:id>/', views.book_detail, name="detail"),
    #path('update/<int:id>/', views.book_update, name="update"),
    #path('delete/<int:id>/', views.book_delete, name="delete"),
]