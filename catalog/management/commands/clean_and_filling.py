import json
import psycopg2
from catalog.models import Category, Product
from django.core.management import BaseCommand


class Command(BaseCommand):

    def cleaning(self, *args, **options):
        with psycopg2.connect(host='localhost', database='django_orm',
                              user='postgres', password='krot123.A') as conn:

            with conn.cursor() as cur:
                cur.execute("DELETE FROM catalog_product")
                cur.execute("DELETE FROM catalog_category")

        conn.close()

    def filling(self, *args, **options):

        create_catalog = []
        create_product = []

        with open('data.json', 'r', encoding='utf-8') as file:
            template = json.load(file)
            for item in template:
                if item["model"] == "catalog.category":
                    categories = {"name": item["fields"]["name"],
                                  "description": item["fields"]["description"]}
                    create_catalog.append(Category(**categories))
                elif item["model"] == "catalog.product":
                    products = {"name": item["fields"]["name"],
                                "description": item["fields"]["description"],
                                "price_for_one": item["fields"]["price_for_one"]}
                    create_product.append(Product(**products))

        Category.objects.bulk_create(create_catalog)
        Product.objects.bulk_create(create_product)