from django.urls import path

from core.views import IndexView, AboutView, DeliveryAndPaymentView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('delivery-and-payment', DeliveryAndPaymentView.as_view(), name='delivery_and_payment'),
]
