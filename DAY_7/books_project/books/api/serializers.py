from ..models import Author, Book
from rest_framework import serializers
from django.utils.timezone import now

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["id", "created_date"]

    def get_author_name(self, obj):
        return f"{obj.author.name}"
    
    def validate(self, value):
        if value == self.initial_data['description']:
            raise serializers.ValidationError(
                f"İsim Alanı: {value} Açıklama Alanı: {self.initial_data['description']} Aynı! Bu iki alan farklı olmalıdır."
            )
        return value
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Fiyat Negatif Bir Değer Alamaz!"
            )
        return value
    
    def validate_name(self, value):
        letters = ["ö", "ü", "ç", "ş", "Ö", "Ü", "Ç", "Ş"]
        for i in value:
            for j in letters:
                raise serializers.ValidationError("İsimde Türkçe karakter olamaz!")
        return value
    
    def get_days_since_joined(self, obj):
        return (now() - obj.created_date).days

    
class AuthorSerializer(serializers.ModelSerializer):
    # Author'ın yazdığı kitapların Serializer'ı, HyperlinkedRelatedField ile belirtiliyor
    books = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="book_detail"
    )

    class Meta:
        model = Author
        fields = "__all__"  # Tüm model alanları dahil ediliyor