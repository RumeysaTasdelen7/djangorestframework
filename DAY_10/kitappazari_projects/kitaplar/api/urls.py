from django.urls import path
from . import views

urlpatterns = [
    path("kitaplar/", views.KitapListCreateAPIView.as_view(), name="kitap_list"),
    path("kitaplar/<int:pk>/", views.KitapDetailAPIView.as_view(), name="kitap_detail"),
    path("kitaplar/<int:pk>/yorum_yap/", views.YorumCreateAPIView.as_view(), name="yorum_create"),
    path("Yorumlar/<int:pk>/", views.YorumDetailAPİView.as_view(), name="yorumlar_detail"),
]