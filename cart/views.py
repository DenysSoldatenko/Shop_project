from django.shortcuts import redirect

from cart.models import Cart
from inventory.models import Product


def cart_add(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    pass


def cart_remove(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    cart = Cart.objects.get(product=product)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
