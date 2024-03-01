from django.urls import path

from inventory.views import ProductView, CatalogView

app_name = 'inventory'

urlpatterns = [
    path('search/', CatalogView.as_view(), name='search'),
    path('<slug:category_slug>/', CatalogView.as_view(), name='product_list'),
    path('product/<slug:product_slug>/', ProductView.as_view(), name='product_detail'),
]
