from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.cart_add, name='add_to_cart'),
    path('update/<int:product_id>/', views.cart_change, name='update_cart_item'),
    path('remove/<int:product_id>/', views.cart_remove, name='remove_from_cart'),
]
