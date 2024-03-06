from django.urls import path

from user.views import UserCartView, UserLoginView, UserRegistrationView, UserProfileView, UserLogoutView

app_name = 'user'

urlpatterns = [
    path('cart/', UserCartView.as_view(), name='cart'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
