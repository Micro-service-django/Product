from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductSerializer(admin.ModelAdmin):
  class Meta:
    model = Product
    fields = (
      'id', 
      'name', 
      'weight', 
      'price'
    )
