from django.http import Http404, JsonResponse
from rest_framework import status
# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView

from Common.CustomPermission.CustomPermission import AdminPermission, UserPermission
from .serializers import *
from .utils import *
from .models import *


class RegisterView(APIView):
    permission_classes = [AdminPermission]

    def get(self, request):
        users = User.objects.filter(is_active=1)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DetailUserApiView(APIView):
    permission_classes = [UserPermission]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        user = self.get_object(id)
        user.is_active = 0
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def hello(request):
    test_param = request.GET.get('input')
    raw_vl = 'giaphien363'
    if test_param is None:
        hex_dig = HashPass(raw_vl)
    else:
        raw_vl = test_param
        hex_dig = HashPass(test_param)

    html = f"raw values: <span style='color:red;'>{raw_vl}</span>  <br> hashed: <span style='color:red;'>{hex_dig}</span>"

    return HttpResponse(html)
