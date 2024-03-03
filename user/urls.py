from django.urls import path
from user import views
from user.views import UserCartView, UserLoginView

app_name = 'user'

urlpatterns = [
    path('cart/', UserCartView.as_view(), name='cart'),
    path('profile/', views.profile, name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
