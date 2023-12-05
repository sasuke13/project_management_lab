import datetime
import jwt
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

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


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email, is_active=True).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        payload = {
            'uuid': str(user.uuid),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(uuid=payload['uuid']).first()
        serializer = UserSerializer(user)

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

    def put(self, request):
        token = request.COOKIES.get('jwt')  # Assuming the token is in a cookie

        if token:
            user = verify_user(token)

            if user:
                user = User.objects.filter(pk=user['uuid']).first()
                serializer = UpdateUserSerializer(user, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'User updated successfully'})

                return Response(serializer.errors)

            return Response({'error': 'Invalid or expired token'})

