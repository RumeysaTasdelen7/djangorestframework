from django.contrib import admin
from .models import Gazeteci, Makale

# Register your models here.

admin.site.register(Gazeteci)
admin.site.register(Makale)