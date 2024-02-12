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
                message = f"The quantity of {product.name} has been increased to {cart.quantity}."
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
            message = f"The item {product.name} has been added to your cart."

    user_cart = get_user_cart_detail(request)
    cart_items_html = render_to_string("cart/cart_details.html", {"cart": user_cart}, request=request)
    response_data = {
        "message": message,
        "cart_items_html": cart_items_html,
    }
    return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")
    cart = Cart.objects.get(id=cart_id)
    changed_product = cart.product
    cart.quantity = quantity
    cart.save()

    response_message = f"The quantity of {changed_product.name} has been updated to {quantity}."

    cart_items_html = render_to_string("cart/cart_details.html", {"cart": get_user_cart_detail(request)},
                                       request=request)
    response_data = {
        "message": response_message,
        "cart_items_html": cart_items_html,
        "quantity": quantity,
    }
    return JsonResponse(response_data)


def cart_remove(request):
    cart_id = request.POST.get("cart_id")
    cart = Cart.objects.get(id=cart_id)
    removed_product = cart.product
    quantity = cart.quantity
    cart.delete()

    message = f"The item {removed_product.name} has been removed from your cart."

    user_cart = get_user_cart_detail(request)
    cart_items_html = render_to_string("cart/cart_details.html", {"cart": user_cart}, request=request)
    response_data = {
        "message": message,
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }
    return JsonResponse(response_data)

