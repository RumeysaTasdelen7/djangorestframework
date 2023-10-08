from rest_framework import serializers
from ..models import Category, Product, Comment


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ['user', 'product']

    def get_user_name(self, obj):
        return obj.user.username
    
    def get_product_name(self, obj):
        return obj.product.title


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

class ProductOfCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['category']