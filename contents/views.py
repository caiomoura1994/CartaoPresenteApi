import json

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Order

from .serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['POST'])
def create_checkout(request):
    raw_payload = str(request.body, 'utf-8')
    payload = json.loads(raw_payload)
    product_id = payload.get('product_id', '')
    amount = payload.get('amount', '')
    domain_url = payload.get('domain_url', '')
    if not product_id:
        raise ValidationError('Produto não encontrado.')
    product = Product.objects.get(pk=product_id)
    new_session = create_checkout_session(product, amount, domain_url)
    if new_session:
        return Response(status=status.HTTP_204_NO_CONTENT, data=new_session)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
