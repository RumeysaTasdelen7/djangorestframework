from django.urls import path
from . import views

urlpatterns = [
    path("makaleler/", views.MakaleListCreateAPView.as_view(), name="makale_list"),
    path("makaleler/<int:pk>/", views.MakaleDetailAPIView.as_view(), name="makale_detail"),
    path("gazeteciler/", views.GazeteciListCreateAPView.as_view(), name="gazeteci_list"),
    path("gazeteciler/<int:pk>/", views.GazeteciDetailAPIView.as_view(), name="gazeteci_detail"),
]