# Generated by Django 4.2.5 on 2023-09-28 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gazeteci",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isim", models.CharField(max_length=120)),
                ("soyisim", models.CharField(max_length=120)),
                ("biyografi", models.TextField(blank=True, max_length=500, null=True)),
            ],
            options={
                "verbose_name": "Gazeteci",
                "verbose_name_plural": "Gazeteciler",
            },
        ),
        migrations.CreateModel(
            name="Makale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("baslik", models.CharField(max_length=120)),
                ("aciklama", models.CharField(max_length=200)),
                ("metin", models.TextField()),
                ("sehir", models.CharField(max_length=120)),
                ("yayinlanma_tarihi", models.DateField()),
                ("aktif", models.BooleanField(default=True)),
                ("yaratilma_tarihi", models.DateTimeField(auto_now_add=True)),
                ("guncelleme_tarihi", models.DateTimeField(auto_now=True)),
                (
                    "yazar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="makale",
                        to="haberler.gazeteci",
                    ),
                ),
            ],
            options={
                "verbose_name": "Makale",
                "verbose_name_plural": "Makaleler",
            },
        ),
    ]
