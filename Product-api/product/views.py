from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .api.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product(request):
  productSerializer = ProductSerializer
  if request.method == 'GET':
    products = Product.objects.all()
    return Response({"results": productSerializer(products, many=True).data })

  if request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)
  
@api_view(['GET', 'DELETE'])
def productDetails(request, id):
  try:
    product = Product.objects.get(id=id)
  except Product.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    productSerializer = ProductSerializer
    return Response(productSerializer(product).data)
  
  if request.method == 'DELETE':
    product.delete()
    return Response(status=status.HTTP_200_OK)
