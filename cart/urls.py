from django.urls import path

from cart.views import CartAddView, CartChangeView, CartRemoveView

app_name = 'cart'

urlpatterns = [
    path('add/', CartAddView.as_view(), name='add_to_cart'),
    path('update/', CartChangeView.as_view(), name='update_cart_item'),
    path('remove/', CartRemoveView.as_view(), name='remove_from_cart'),
]
