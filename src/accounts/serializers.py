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
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
