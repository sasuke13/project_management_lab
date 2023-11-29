from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response

from accounts.models import User
from accounts.views import verify_user
from orders.models import Orders, States
from orders.serializers import OrdersSerializer


# Create your views here.
class OrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class CreateOrderView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def create(self, request, *args, **kwargs):
        state = 'NW'

        token = request.COOKIES.get('jwt')
        payload = verify_user(token)
        client = User.objects.filter(uuid=payload['uuid']).first()

        with transaction.atomic():
            order_history_instance = States.objects.create(states=[state])

            order = Orders.objects.create(state=state, client=client, order_history=order_history_instance)

        serializer = self.get_serializer(order)
        return Response({'message': 'Order was successfully opened', 'order': serializer.data}, status=status.HTTP_201_CREATED)

