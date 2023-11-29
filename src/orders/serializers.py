# serializers.py
from rest_framework import serializers

from accounts.models import User
from .models import Orders


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'surname', 'email', 'phone_number', 'address')


class OrdersSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Orders
        fields = '__all__'
        read_only_fields = ('id', 'state', 'order_history', 'client', 'grant_date')
