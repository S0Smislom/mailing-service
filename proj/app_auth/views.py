from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import yandex_service, user_service
from .serializers import UserSerializer, YandexSerializer, LoginSerializer


# Create your views here.
class LoginView(APIView):
    serializer_class = LoginSerializer

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        validated_data = data.validated_data
        user = authenticate(request, username=validated_data.get('email'), password=validated_data.get('password'))
        if not user:
            return Response('Wrong login or password', status=401)
        login(request, user)
        return Response(UserSerializer(user).data)


class YandexLoginView(APIView):

    def get(self, request):
        return HttpResponseRedirect(yandex_service.get_oauth_link())


class YandexLoginRedirectView(APIView):

    def get(self, request):
        yandex_serializer = YandexSerializer(data=request.GET)
        yandex_serializer.is_valid(raise_exception=True)
        validated_data = yandex_serializer.validated_data

        code = validated_data.get('code')
        error = validated_data.get('error')
        if error or not code:
            return Response(False)
            
        try:
            user = yandex_service.authenticate(code)
        except Exception as e:
            return Response(e.args, status=400)
        login(request, user=user)
        return Response(UserSerializer(user).data)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        logout(request)
        return Response(True)