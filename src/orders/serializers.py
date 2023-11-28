# serializers.py
from rest_framework import serializers

from accounts.models import User
from .models import Orders


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'surname', 'email', 'phone_number', 'address')


class OrdersModelSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Orders
        fields = ('id', 'state', 'grant_date', 'client', 'order_history')
