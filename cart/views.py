from django.http import JsonResponse
from django.views.generic import View
from cart.services import CartAddService, CartChangeService, CartRemoveService
from cart.mixins import render_cart
from inventory.models import Product


class CartAddView(View):
    def post(self, request):
        product = Product.objects.get(id=request.POST.get("product_id"))
        cart_service = CartAddService(request, product)
        cart_service.add_product_to_cart()

        return JsonResponse({
            "message": f"{product.name} has been added to your cart.",
            "cart_items_html": render_cart(request)
        })


class CartChangeView(View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        new_quantity = int(request.POST.get("quantity"))
        cart_service = CartChangeService(request, cart_id, new_quantity)
        cart = cart_service.update_cart_item()

        return JsonResponse({
            "message": f"The quantity of {cart.product.name} has been updated to {cart.quantity}.",
            "quantity": cart.quantity,
            "cart_items_html": render_cart(request)
        })


class CartRemoveView(View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        cart_service = CartRemoveService(request, cart_id)
        product, quantity = cart_service.remove_cart_item()

        return JsonResponse({
            "message": f"{product.name} has been removed from your cart.",
            "cart_items_html": render_cart(request),
            "quantity_deleted": quantity,
        })
