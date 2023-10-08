from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    page_number = models.IntegerField()
    publish_date = models.DateField()
    stock = models.IntegerField()

    class Meta:
        verbose_name = "kitap"
        verbose_name_plural = "kitaplar"
        ordering = ["publish_date"]

    def __str__(self):
        return self.title