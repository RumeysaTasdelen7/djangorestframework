from rest_framework import serializers
from ..models import Author, Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author_name = serializers.SerializerMethodField()
    author_id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    created_date = serializers.DateTimeField(read_only=True)
    activate = serializers.BooleanField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.author_id = validated_data.get("author_id", instance.author_id)
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.created_date = validated_data.get("created_date", instance.created_date)
        instance.activate = validated_data.get("activate", instance.activate)
        instance.save()

        return instance
    
    def get_author_name(self, obj):
        return f"{obj.author.name}"
    
    def validate_name(self, value):
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


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    bio = serializers.CharField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.bio = validated_data.get("bio", instance.bio)
        
        instance.save()

        return instance