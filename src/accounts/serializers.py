from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        instance.save()
        return instance
