import os
import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand
from django.db import IntegrityError
from faker import Faker

from cart.models import Cart
from inventory.models import Category, Product
from user.models import User
from order.models import Order, OrderItem
from PIL import Image
from io import BytesIO

class Command(BaseCommand):
    help = "Generate fake data for Category, Product, Cart, and Order models"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Step 1: Create Categories
        categories = []
        for _ in range(5):
            category_name = fake.word().capitalize()
            category_slug = fake.slug()

            try:
                category = Category.objects.create(
                    name=category_name,
                    slug=category_slug
                )
                categories.append(category)
                self.stdout.write(self.style.SUCCESS(f'Successfully created category: {category.name}'))

            except IntegrityError:
                self.stdout.write(self.style.WARNING(
                    f'Category name or slug "{category_name}" already exists. Skipping this category.'))
                continue

        # Step 2: Create Products
        products = []
        for _ in range(35):
            product_name = fake.word().capitalize()
            product_slug = fake.slug()
            product_description = fake.text()
            product_image_url = fake.image_url()
            product_price = round(fake.random_number(digits=2) + fake.random_number(digits=2) / 100, 2)
            product_discount = fake.random_int(min=0, max=50)
            product_quantity = fake.random_int(min=1, max=100)
            product_category = fake.random_element(categories)

            try:
                response = requests.get(product_image_url)
                if response.status_code == 200:
                    image_name = os.path.basename(product_image_url)
                    if not image_name.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp')):
                        image_name += '.jpg'

                    image = Image.open(BytesIO(response.content))

                    # Convert palette-based (P) images to RGB before saving as JPEG
                    if image.mode != 'RGB':
                        image = image.convert('RGB')

                    # Resize the image to a fixed size (e.g., 300x300)
                    image = image.resize((300, 300))

                    image_io = BytesIO()
                    image.save(image_io, format='JPEG')
                    image_io.seek(0)

                    image_content = ContentFile(image_io.read(), name=image_name)

                    product = Product.objects.create(
                        name=product_name,
                        slug=product_slug,
                        description=product_description,
                        image=image_content,
                        price=product_price,
                        discount=product_discount,
                        quantity=product_quantity,
                        category=product_category
                    )
                    products.append(product)
                    self.stdout.write(self.style.SUCCESS(f'Successfully created product: {product.name}'))

                else:
                    self.stdout.write(self.style.WARNING(f'Failed to download image for product "{product_name}". HTTP status: {response.status_code}'))

            except IntegrityError:
                self.stdout.write(self.style.WARNING(f'Product name "{product_name}" already exists. Skipping this product.'))
                continue

            except requests.RequestException as e:
                self.stdout.write(self.style.WARNING(f'Failed to download image for product "{product_name}". Error: {e}'))
                continue

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
                continue

        # Step 3: Create Users
        users = []
        for _ in range(10):
            username = fake.user_name()
            password = 'password'
            email = fake.email()
            phone_number = fake.phone_number()[:10]

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                phone_number=phone_number
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user.username}'))

        # Step 4: Generate Carts for Users
        for user in users:
            for _ in range(fake.random_int(1, 5)):  # Each user can have between 1 to 5 cart items
                product = fake.random_element(products)
                quantity = fake.random_int(1, 3)
                Cart.objects.create(
                    user=user,
                    product=product,
                    quantity=quantity
                )
                self.stdout.write(self.style.SUCCESS(f'User {user.username} added product {product.name} to cart.'))

        # Step 5: Generate Orders from Carts
        for user in users:
            cart_items = Cart.objects.filter(user=user)
            if not cart_items:
                continue

            # Create an order for the user
            phone_number = fake.phone_number()[:10]
            requires_delivery = fake.boolean()
            delivery_address = fake.address() if requires_delivery else None
            payment_on_get = fake.boolean()

            order = Order.objects.create(
                user=user,
                phone_number=phone_number,
                requires_delivery=requires_delivery,
                delivery_address=delivery_address,
                payment_on_get=payment_on_get,
                is_paid=fake.boolean(),
                status="Processing"
            )

            # Add order items based on cart items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    name=cart_item.product.name,
                    price=cart_item.product.price,
                    quantity=cart_item.quantity
                )

            self.stdout.write(self.style.SUCCESS(f'Order for user {user.username} created with {cart_items.count()} items.'))

            # Optional: Clear cart after order is created
            cart_items.delete()