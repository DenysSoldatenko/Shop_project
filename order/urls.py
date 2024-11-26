from django.urls import path

from order.views import CreateOrderView

app_name = 'order'

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='create_order'),
]
