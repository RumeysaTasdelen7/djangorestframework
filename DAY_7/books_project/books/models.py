from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)

    class Meta:
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    name = models.CharField(max_length=150, verbose_name="isim")
    description = models.TextField(max_length=500, verbose_name="Açıklama")
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)


    class Meta:
        verbose_name = "Kitap"
        verbose_name_plural = "Kitaplar"

    def __str__(self):
        return self.name