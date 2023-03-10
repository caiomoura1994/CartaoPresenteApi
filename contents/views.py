import json

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Order
from services.stripe import create_checkout_session

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
    product_slug = payload.get('product_slug', '')
    amount = payload.get('amount', '')
    domain_url = payload.get('domain_url', '')
    if not product_slug:
        raise ValidationError('Produto não encontrado.')
    product = Product.objects.get(slug=product_slug)
    new_session = create_checkout_session(product, amount, domain_url)
    if new_session:
        return Response(new_session)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def check_order_by_session(request):
    session_checkout_id = request.GET.get('sessionCheckoutId', None)
    order = Order.objects.get(stripe_checkout_key=session_checkout_id)
    order.gift_code = "Codigo_gift_card234"
    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)