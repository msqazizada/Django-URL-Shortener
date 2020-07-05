from django.urls import path

from .views import home, redirect_to_original_url, about

app_name = 'url_shortener'

urlpatterns = [
    path('', home, name='home'),
    path('<str:shortened_url>/', redirect_to_original_url, name='url'),
    path('about/', about, name='about'),
]
