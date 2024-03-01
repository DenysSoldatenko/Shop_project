from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from inventory.models import Product
from inventory.utils import q_search


class CatalogView(ListView):
    model = Product
    template_name = "inventory/product_list.html"
    context_object_name = "products"
    paginate_by = 3
    allow_empty = False
    slug_url_kwarg = "category_slug"

    def get_queryset(self):
        category_slug = self.kwargs.get(self.slug_url_kwarg)
        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("query")

        if category_slug == "all":
            inventory = super().get_queryset()
        elif query:
            inventory = q_search(query)
        else:
            inventory = super().get_queryset().filter(category__slug=category_slug)
            if not inventory.exists():
                raise Http404()

        if on_sale:
            inventory = inventory.filter(discount__gt=0)

        if order_by and order_by != "default":
            inventory = inventory.order_by(order_by)

        return inventory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Catalog"
        context["slug_url"] = self.kwargs.get(self.slug_url_kwarg)
        return context


class ProductView(DetailView):
    template_name = "inventory/product_detail.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        return get_object_or_404(Product, slug=self.kwargs.get(self.slug_url_kwarg))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context
