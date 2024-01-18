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
    # Optional: You can log or debug context variables here
    # print(context['title'])
    # print(context['slug_url'])
    # print(context['goods'])
    # print([product.name for product in context['goods']])
    query.update(kwargs)
    return urlencode(query)
