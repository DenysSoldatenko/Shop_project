from django import template

from cart.utils import get_user_cart_detail

register = template.Library()


@register.simple_tag()
def get_user_cart(request):
    return get_user_cart_detail(request)
