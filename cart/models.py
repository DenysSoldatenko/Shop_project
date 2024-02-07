from django.db import models

from inventory.models import Product
from user.models import User


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.get_product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Quantity')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Date Added')

    class Meta:
        db_table = 'carts'
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ("id",)

    objects = CartQueryset().as_manager()

    def get_product_price(self):
        return round(self.product.get_sale_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'

        return f'Anonymous Cart | Product {self.product.name} | Quantity {self.quantity}'
