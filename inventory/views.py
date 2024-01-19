from django.shortcuts import render

from inventory.models import Product


def product_list(request):
    context = {
        "title": "Product Catalog",
        "products": Product.objects.all(),
    }
    return render(request, "inventory/product_list.html", context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {"product": product}
    return render(request, "inventory/product_detail.html", context)
