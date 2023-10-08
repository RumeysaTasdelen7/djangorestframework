from django.db import models

# Create your models here.

class Gazeteci(models.Model):
    isim = models.CharField(max_length=120)
    soyisim = models.CharField(max_length=120)
    biyografi = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.isim} {self.soyisim}"
    
    class Meta:
        verbose_name = "Gazeteci"
        verbose_name_plural = "Gazeteciler"


class Makale(models.Model):
    yazar = models.ForeignKey(Gazeteci, on_delete=models.CASCADE, related_name="makale")
    baslik = models.CharField(max_length=120)
    aciklama = models.CharField(max_length=200)
    metin = models.TextField()
    sehir = models.CharField(max_length=120)
    yayimlanma_tarihi = models.DateField()
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baslik
    
    class Meta:
        verbose_name = "Makale"
        verbose_name_plural = "Makaleler"