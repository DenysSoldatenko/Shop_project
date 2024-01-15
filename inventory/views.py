from django.shortcuts import render

from inventory.models import Product


def catalog(request):
    context = {
        "title": "Home - Catalog",
        "goods": Product.objects.all(),
    }
    return render(request, "inventory/catalog.html", context)


def product(request):
    return render(request, "inventory/product.html")
