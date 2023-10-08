from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookAPIView.as_view()),
]

# localhost:8000/api