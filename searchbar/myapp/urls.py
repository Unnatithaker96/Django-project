# urls.py

from django.urls import path
from .views import productsearch

urlpatterns = [
    path('', productsearch, name='productsearch'),
]
