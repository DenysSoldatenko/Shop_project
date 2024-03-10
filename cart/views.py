from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import View
from cart.mixins import get_cart, render_cart
from cart.models import Cart
from cart.utils import get_user_cart_detail
from inventory.models import Product


class CartAddView(View):
    def post(self, request):
        product = Product.objects.get(id=request.POST.get("product_id"))
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

        return JsonResponse({
            "message": f"{product.name} has been added to your cart!",
            "cart_items_html": render_cart(request)
        })


class CartChangeView(View):
    def post(self, request):
        cart = get_cart(request, cart_id=request.POST.get("cart_id"))
        cart.quantity = request.POST.get("quantity")
        cart.save()

        return JsonResponse({
            "message": f"The quantity of {cart.product.name} has been updated to {cart.quantity}!",
            "quantity": cart.quantity,
            "cart_items_html": render_cart(request)
        })


class CartRemoveView(View):
    def post(self, request):
        cart = get_cart(request, cart_id=request.POST.get("cart_id"))
        product, quantity = cart.product, cart.quantity
        cart.delete()

        return JsonResponse({
            "message": f"{product.name} has been removed from your cart.",
            "cart_items_html": render_to_string(
                "cart/cart_details.html",
                {"cart": get_user_cart_detail(request)},
                request=request
            ),
            "quantity_deleted": quantity,
        })
