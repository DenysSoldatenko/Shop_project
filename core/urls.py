from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='index'),
    path('about', views.about_us, name='about'),
]