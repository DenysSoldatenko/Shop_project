from django.urls import path

from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
]