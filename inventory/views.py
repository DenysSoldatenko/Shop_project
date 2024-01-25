from django.core.paginator import Paginator
from django.shortcuts import render

from inventory.models import Product
from inventory.utils import q_search


def product_list(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', 'default')
    query = request.GET.get('query', None)

    if category_slug == "all":
        products = Product.objects.all()
    elif query:
        products = q_search(query)
    else:
        products = Product.objects.filter(category__slug=category_slug)

    if on_sale:
        products = products.filter(discount__gt=0)
    if order_by != 'default':
        products = products.order_by(order_by)

    paginator = Paginator(products, 6)
    current_page = paginator.get_page(page)

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
