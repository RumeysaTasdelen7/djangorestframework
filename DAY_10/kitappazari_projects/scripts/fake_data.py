import os
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kitap_pazari.settings")

import django
django.setup()


from django.contrib.auth.models import User

from faker import Faker
import requests

def set_user():
    fake = Faker(['tr_TR'])
    first_name = fake.first_name()
    last_name = fake.last_name()
    user_name = f"{first_name.lower()}_{last_name.lower()}"
    email = f"{user_name}@{fake.domain_name}"
    print(first_name, last_name, email)

    user_check = User.objects.filter(username=user_name)

    while user_check.exists():
        user_name = user_name + str(random.randrange(1, 99))
        user_check = User.objects.filter(username=user_name)

    user = User(
        username = user_name,
        first_name = first_name,
        last_name = last_name,
        email = email,
        is_staff = fake.boolean(chance_of_getting_true=50)
    )

    user.set_password("Testing321.")
    user.save()
    print("Kullanıcı kaydedildi", user_name)


from pprint import pprint
from kitaplar.api.serializers import KitapSerializer

def kitap_ekle(konu):
    fake = Faker(['tr_TR'])
    url = "https://openlibrary.org/search.json"
    payload = {"q": konu}
    response = requests.get(url, params=payload)

    if response.status_code != 200:
        print("Hatalı istek yapıldı", response.status_code)
        return
        
    jsn = response.json()
    kitaplar = jsn.get("docs")

    for kitap in kitaplar:
        kitap_adi = kitap.get("title")
        data = dict(
            isim = kitap_adi,
            yazar = kitap.get('author_name')[0],
            yayin_tarihi = fake.date_time_between(start_date="-10y", end_date="now", tzinfo=None)
        )

        serializer = KitapSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('kitap kaydedildi: ', kitap_adi)
        else:
            continue