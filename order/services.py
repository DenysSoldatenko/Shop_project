from django.db import transaction
from django.core.exceptions import ValidationError
from cart.models import Cart
from order.models import Order, OrderItem


class OrderService:
    def __init__(self, user, form_data):
        self.user = user
        self.form_data = form_data

    def create_order(self):
        with transaction.atomic():
            cart_items = Cart.objects.filter(user=self.user)

            if not cart_items.exists():
                raise ValidationError('Your cart is empty.')

            order = Order.objects.create(
                user=self.user,
                phone_number=self.form_data['phone_number'],
                requires_delivery=self.form_data['requires_delivery'],
                delivery_address=self.form_data['delivery_address'],
                payment_on_get=self.form_data['payment_on_get'],
            )

            for cart_item in cart_items:
                self._process_cart_item(cart_item, order)

            cart_items.delete()

    def _process_cart_item(self, cart_item, order):
        product = cart_item.product
        if product.quantity < cart_item.quantity:
            raise ValidationError(f'Insufficient stock for product {product.name}. Available stock: {product.quantity}.')

        OrderItem.objects.create(
            order=order,
            product=product,
            name=product.name,
            price=product.get_sale_price(),
            quantity=cart_item.quantity,
        )

        product.quantity -= cart_item.quantity
        product.save()
