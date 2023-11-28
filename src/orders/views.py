from rest_framework import generics

from orders.models import Orders
from orders.serializers import OrdersModelSerializer


# Create your views here.
class OrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersModelSerializer
