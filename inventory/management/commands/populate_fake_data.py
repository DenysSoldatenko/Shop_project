from django.core.management.base import BaseCommand
from django.db import IntegrityError
from faker import Faker

from inventory.models import Category, Product


class Command(BaseCommand):
    help = "Generate fake data for Category and Product models"

    def handle(self, *args, **kwargs):
        fake = Faker()

        categories = []
        for _ in range(10):
            category_name = fake.word().capitalize()
            category_slug = fake.slug()

            try:
                category = Category.objects.create(
                    name=category_name,
                    slug=category_slug
                )
                categories.append(category)
                self.stdout.write(self.style.SUCCESS(f'Successfully created category: {category.name}'))

            except IntegrityError as e:
                self.stdout.write(self.style.WARNING(
                    f'Category name or slug "{category_name}" already exists. Skipping this category.'))
                continue

        for _ in range(20):
            product_name = fake.word().capitalize()
            product_slug = fake.slug()
            product_description = fake.text()
            product_image = fake.image_url()
            product_price = round(fake.random_number(digits=2) + fake.random_number(digits=2) / 100, 2)
            product_discount = fake.random_int(min=0, max=50)
            product_quantity = fake.random_int(min=1, max=100)
            product_category = fake.random_element(categories)

            try:
                product = Product.objects.create(
                    name=product_name,
                    slug=product_slug,
                    description=product_description,
                    image=product_image,
                    price=product_price,
                    discount=product_discount,
                    quantity=product_quantity,
                    category=product_category
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully created product: {product.name}'))

            except IntegrityError as e:
                self.stdout.write(
                    self.style.WARNING(f'Product name "{product_name}" already exists. Skipping this product.'))
                continue
