from rest_framework import serializers
from ..models import Gazeteci, Makale

from datetime import datetime, date
from django.utils.timesince import timesince


class MakaleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Makale
        fields = "__all__"
        read_only_fields = ["id", "yaratilma_tarihi", "guncelleme_tarihi"]
        
    def get_time_since_publication(self, object):
        now = datetime.now()
        pub_date = object.yayimlanma_tarihi
        if object.aktif == True:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return 'Aktif değil'
        
    def validate_yayimlanma_tarihi(self, tarihdegeri):
        today = date.today()

        if tarihdegeri > today:
            serializers.ValidationError("Yayımlanma tarihi ileri bir tarih olamaz")

            return tarihdegeri
    def get_gazeteci(self):
        return f"{object.yazar.isim} {object.yazar.soyisim}"
        
class GazeteciSerializer(serializers.ModelSerializer):

    makaleler = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="makale_detay")

    class Meta:
        model = Gazeteci
        fields = "__all__"