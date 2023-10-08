from rest_framework.generics import get_object_or_404

from rest_framework import generics
from rest_framework import permissions
from .permissions import IsAdminUserOrReadonly, IsYorumSahibiOrReadOnly
from .pagination import SmallPagination, LargePagination
from rest_framework.exceptions import ValidationError

from kitaplar.models import Kitap, Yorum
from .serializers import KitapSerializer, YorumSerializer



class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all().order_by("id")
    serializer_class = KitapSerializer
    permission_classes = [IsAdminUserOrReadonly]
    pagination_class = LargePagination

class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    permission_classes = [IsAdminUserOrReadonly]

class YorumCreateAPIView(generics.CreateAPIView):
    queryset=Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get("kitap_pk")
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        kullanici = self.request.user
        yorumlar = Yorum.objects.filter(kitap=kitap, yorum_sahibi=kullanici)

        if yorumlar.exists():
            raise ValidationError('Bir kitaba sadece  bir yorum yapabilirsiniz ')
        serializer.save(kitap=kitap, yorum_sahibi=kullanici)

class YorumDetailAPİView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsYorumSahibiOrReadOnly]