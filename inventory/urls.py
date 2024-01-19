from django.urls import path

from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.product_list, name='index'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
]