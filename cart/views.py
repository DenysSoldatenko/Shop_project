from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import View

from cart.mixins import get_cart, render_cart
from cart.models import Cart
from cart.utils import get_user_cart_detail
from inventory.models import Product


class CartAddView(View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)

        cart = get_cart(request, product=product)

        if cart:
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(
                user=request.user if request.user.is_authenticated else None,
                session_key=request.session.session_key if not request.user.is_authenticated else None,
                product=product,
                quantity=1
            )

        response_data = {
            "message": f"The item {product.name} has been added to your cart!",
            'cart_items_html': render_cart(request)
        }

        return JsonResponse(response_data)


class CartChangeView(View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        cart = get_cart(request, cart_id=cart_id)
        changed_product = cart.product

        cart.quantity = request.POST.get("quantity")
        cart.save()

        quantity = cart.quantity

        response_data = {
            "message": f"The quantity of {changed_product.name} has been updated to {quantity}!",
            "quantity": quantity,
            'cart_items_html': render_cart(request)
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
