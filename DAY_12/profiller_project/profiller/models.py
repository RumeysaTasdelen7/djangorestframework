from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from PIL import Image

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profil")
    bio = models.CharField(max_length=300, blank=True, null=True)
    sehir = models.CharField(max_length=120, blank=True, null=True)
    foto = models.ImageField(null=True, blank=True, upload_to="profil_fotolari/%Y/%m")

    class Meta:
        verbose_name_plural = 'Profiller'

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.foto:
            img = Image.open(self.foto.path)
            if img.height > 600 or img.width > 600:
                output_size =(600, 600)
                img.thumbnail(output_size)
                img.save(self.foto.path)


class ProfilDurum(models.Model):
    user_profile = models.ForeignKey(Profil, on_delete=models.CASCADE)
    durum_mesaji = models.CharField(max_length=200)
    yaratilma_zamani = models.DateTimeField(auto_now_add=True)
    guncellenme_zamani = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Profil Mesajları'


    def __str__(self):
        return str(self.user_profil)
    
    