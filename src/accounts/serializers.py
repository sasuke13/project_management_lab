from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone_number', 'address']
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'phone_number': {'required': True},
            'address': {'required': True},

        }

    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        instance.save()
        return instance


class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'password', 'phone_number']

        extra_kwargs = {
            'name': {'required': True},
            'surname': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'phone_number': {'required': True},
        }

    def create(self, validated_data):
        instance = User.objects.create_superuser(**validated_data)
        instance.save()
        return instance
