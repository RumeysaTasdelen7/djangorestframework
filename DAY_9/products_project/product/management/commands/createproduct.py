import requests
from ...models import Category, Product
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        url_product = "https://dummyjson.com/products"
        url_category = "https://dummyjson.com/products/categories"

        response_products = requests.get(url_product)
        response_categories = requests.get(url_category)


        products = response_products.json()
        categories = response_categories.json()
        for category_name in categories:
            category = Category.objects.create(
                name=category_name
            )
            for product in products['products']:
                if product['category'] == category_name:
                    Product.objects.get_or_create(
                        title=product['title'],
                        description=product['description'],
                        price=product['price'],
                        stock=product['stock'],
                        brand=product['brand'],
                        category=category,

                    )

        print("Ürünler Kaydedildi")