from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
