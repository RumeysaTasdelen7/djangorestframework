from ..models import Author, Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["id", "created_date"]

    def get_author_name(self, obj):
        return f"{obj.author.name}"
    
class AuthorSerializer(serializers.ModelSerializer):
    # books = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name=)

    class Meta:
        model = Author
        fields = "__all__"