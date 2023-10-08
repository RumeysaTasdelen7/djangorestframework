from typing import Any
import requests
from ...models import Category, Product
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify

class Command(BaseCommand):

    def handle(self, *args, **options):
        from faker import Faker
        fake = Faker('tr_TR')
        for i in range(51):
            user = User.objects.create(
                username=slugify(fake.name()),
                is_staff = False,
                is_superuser = False
            )
            user.set_password('123456')
            user.save()