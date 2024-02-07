from django.urls import path
from user import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('logout/', views.logout, name='logout'),
]
