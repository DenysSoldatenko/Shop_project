from django.template.loader import render_to_string
from django.urls import reverse

from cart.models import Cart
from cart.utils import get_user_cart_detail


def get_cart(request, product=None, cart_id=None):
    if request.user.is_authenticated:
        query_kwargs = {"user": request.user}
    else:
        query_kwargs = {"session_key": request.session.session_key}

    if product:
        query_kwargs["product"] = product

    if cart_id:
        query_kwargs["id"] = cart_id

    return Cart.objects.filter(**query_kwargs).first()


def render_cart(request):
    user_cart = get_user_cart_detail(request)
    context = {"cart": user_cart}

    # if referer page is create_order add key orders: True to context
    referer = request.META.get('HTTP_REFERER')
    if reverse('order:create_order') in referer:
        context["order"] = True

    return render_to_string(
        "cart/cart_details.html",
        context,
        request=request
    )
