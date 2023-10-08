from django.urls import path
from profiller.api.views import ProfilViewSet, ProfilDurumViewSet, ProfilFotoUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profiller", ProfilViewSet, basename="profil")
router.register(r"durum", ProfilDurumViewSet, basename="durum")

urlpatterns = [
    path("profil_foto", ProfilFotoUpdateView.as_view(), name="profil_foto"),
]

urlpatterns += router.urls