from django.urls import path
from cart import views
from cart.views import CartAddView

app_name = 'cart'

urlpatterns = [
    path('add/', CartAddView.as_view(), name='add_to_cart'),
    path('update/', views.cart_change, name='update_cart_item'),
    path('remove/', views.cart_remove, name='remove_from_cart'),
]
