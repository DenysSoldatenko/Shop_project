from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from cart.models import Cart
from cart.utils import get_user_cart_detail

from inventory.models import Product


def cart_add(request):
    product_id = request.POST.get("product_id")
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    user_cart = get_user_cart_detail(request)
    cart_items_html = render_to_string("cart/cart_details.html", {"cart": user_cart}, request=request)
    response_data = {
        "message": "Item was added to the cart",
        "cart_items_html": cart_items_html,
    }
    return JsonResponse(response_data)


def cart_change(request):
    pass


def cart_remove(request):
    cart_id = request.POST.get("cart_id")
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()
    user_cart = get_user_cart_detail(request)
    cart_items_html = render_to_string("cart/cart_details.html", {"cart": user_cart}, request=request)
    response_data = {
        "message": "Item was removed from the cart",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }
    return JsonResponse(response_data)
