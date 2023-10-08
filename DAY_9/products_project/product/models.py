from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    brand = models.CharField(max_length=75)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    RATING_PRODUCT = (
        ('1', 'Çok Kötü'),
        ('2', 'Kötü'),
        ('3', 'İyi'),
        ('4', 'Çok İyi'),
    )

    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(max_length=500, blank=True, null=True)
    rating = models.CharField(choices=RATING_PRODUCT, max_length=10)

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"

    def __str__(self):
        return self.comment