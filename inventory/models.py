from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ("id",)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    image = models.ImageField(upload_to='inventory_images', blank=True, null=True, verbose_name='Image')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Price')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Discount (%)')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Category')

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name} Quantity - {self.quantity}'

    def get_absolute_url(self):
        return reverse("inventory:product_detail", kwargs={"product_slug": self.slug})

    def get_formatted_id(self):
        return f"{self.id:05}"

    def get_sale_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
