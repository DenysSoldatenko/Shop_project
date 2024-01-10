from django.db import models


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
