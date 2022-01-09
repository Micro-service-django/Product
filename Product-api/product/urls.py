from django.urls import path

from .views import product, productDetails

urlpatterns = [
  path('products', product),
  path('products/<str:id>', productDetails),
]