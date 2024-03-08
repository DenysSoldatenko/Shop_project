from django.urls import path
from cart import views
from cart.views import CartAddView, CartChangeView

app_name = 'cart'

urlpatterns = [
    path('add/', CartAddView.as_view(), name='add_to_cart'),
    path('update/', CartChangeView.as_view(), name='update_cart_item'),
    path('remove/', views.cart_remove, name='remove_from_cart'),
]
