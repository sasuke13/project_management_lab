import datetime
import jwt
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .exceptions import PasswordIsInvalid
from .models import User
from .serializers import UserSerializer, SuperUserSerializer, UpdateUserSerializer


def verify_user(token):
    if not token:
        raise AuthenticationFailed('Unauthenticated')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated')

    return payload


class CreateSuperuserView(APIView):
    def post(self, request):
        serializer = SuperUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Superuser created successfully"})

        return Response(serializer.errors)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except PasswordIsInvalid as exception:
            return Response({'error': exception.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response(serializer.data)


class LogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response


class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        # token = request.COOKIES.get('jwt')  # Assuming the token is in a cookie
        #
        # if token:
        #     user = verify_user(token)
        #
        #     if user:
        #         user = User.objects.filter(pk=user['uuid']).first()
        serializer = UpdateUserSerializer(request.user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated successfully'})

        return Response(serializer.errors)

        # return Response({'error': 'Invalid or expired token'})
