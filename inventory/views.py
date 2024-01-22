from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from inventory.models import Product


def product_list(request, category_slug):
    page = request.GET.get('page', 1)
    if category_slug == "all":
        products = Product.objects.all()
    else:
        products = get_list_or_404((Product.objects.filter(category__slug=category_slug)))

    paginator = Paginator(products, 6)
    current_page = paginator.page(int(page))

    context = {
        "title": "Product Catalog",
        "products": current_page,
        "slug_url": category_slug
    }
    return render(request, "inventory/product_list.html", context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {"product": product}
    return render(request, "inventory/product_detail.html", context)
