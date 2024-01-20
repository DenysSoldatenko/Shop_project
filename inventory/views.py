from django.shortcuts import render, get_object_or_404, get_list_or_404

from inventory.models import Product


def product_list(request, category_slug):
    if category_slug == "all":
        products = Product.objects.all()
    else:
        products = get_list_or_404((Product.objects.filter(category__slug=category_slug)))

    context = {
        "title": "Product Catalog",
        "products": products,
    }
    return render(request, "inventory/product_list.html", context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {"product": product}
    return render(request, "inventory/product_detail.html", context)
