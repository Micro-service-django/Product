from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .api.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product(request):
  productSerializer = ProductSerializer
  if request.method == 'GET':
    products = Product.objects.all()
    return Response({"results": productSerializer(products, many=True).data }, status=201)

  if request.method == 'POST':
    product = Product()
    product.name = request.data['name']
    product.weight= request.data['weight']
    product.save()
    return Response(ProductSerializer(product).data, status=201)
