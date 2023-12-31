from datetime import datetime, timedelta

from django.db import transaction
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from orders.models import Orders, States
from orders.serializers import OrdersSerializer


class OrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def get_queryset(self):
        request_data = dict(self.request.GET.lists())
        request_data = dict([(key, value[0]) for key, value in request_data.items()])

        queryset = Orders.objects.all()

        if request_data.get('days'):
            days = request_data.pop('days')
            today_date = datetime.now()
            queryset = queryset.filter(created_at__range=[today_date - timedelta(days=float(days)), today_date])

        queryset = queryset.filter(**request_data)

        return queryset


class UserOrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Orders.objects.filter(client=self.request.user).exclude(state__in=['CNL', 'PD'])

        return queryset


class SpecifiedUserOrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_data = dict(self.request.GET.lists())
        request_data = dict([(key, value[0]) for key, value in request_data.items()])

        queryset = Orders.objects.filter(client=self.request.user)
        queryset = queryset.filter(**request_data)

        return queryset


class SentOrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Orders.objects.filter(client=self.request.user, state='SNT')

        return queryset


class DeliveredOrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Orders.objects.filter(client=self.request.user, state='DLV')

        return queryset


class CreateOrderView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        state = 'NW'

        client = request.user

        with transaction.atomic():
            order_history_instance = States.objects.create(states=[state])

            order = Orders.objects.create(state=state, client=client, order_history=order_history_instance)

        serializer = self.get_serializer(order)
        return Response({
            'message': 'Order was successfully opened',
            'order': serializer.data
        }, status=status.HTTP_201_CREATED)
