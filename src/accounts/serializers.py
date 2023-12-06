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


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone_number']

        extra_kwargs = {
            'name': {'required': False},
            'email': {'required': False},
            'password': {'write_only': True, 'required': False},
            'phone_number': {'required': False},
        }

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        password = validated_data.get('password')

        if password:
            instance.set_password(password)

        instance.save()
        return instance
