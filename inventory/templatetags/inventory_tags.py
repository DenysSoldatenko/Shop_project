from django import template
from django.utils.http import urlencode
from inventory.models import Category

register = template.Library()


@register.simple_tag()
def get_all_categories():
    return Category.objects.all()


@register.simple_tag(takes_context=True)
def update_query_params(context, **kwargs):
    query = context['request'].GET.dict()
    print("\n=== DEBUGGING update_query_params ===")
    print(f"Current request URL: {context['request'].build_absolute_uri()}")
    print("Existing query parameters:", query)
    query.update(kwargs)
    print("Updated query parameters:", query)
    return urlencode(query)
