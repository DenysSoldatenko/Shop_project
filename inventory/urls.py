from django.urls import path

from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('search/', views.product_list, name='search'),
    path('<slug:category_slug>/', views.product_list, name='product_list'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
