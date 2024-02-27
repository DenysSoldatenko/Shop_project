from django.urls import path

from core.views import IndexView, AboutView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
]
