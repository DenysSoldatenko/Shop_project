from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('add/<slug:product_slug>/', views.cart_add, name='add_to_cart'),
    path('update/<slug:product_slug>/', views.cart_change, name='update_cart_item'),
    path('remove/<slug:product_slug>/', views.cart_remove, name='remove_from_cart'),
]
