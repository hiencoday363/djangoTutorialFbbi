import re
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *


class ImgPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_path
        fields = ['id', 'file_name', 'image_url']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'client', 'email', 'phone', 'password', 'nickname']

        extra_kwargs = {
            'password': {
                'required': True,
                'write_only': True
            },
            'email': {
                'required': True,
            },
            'client': {
                'required': True,
            }
        }

    def validate_email(self, email: str) -> str:
        pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        check = pattern.search(email)
        if check is None:
            raise serializers.ValidationError("You have to provide email address!")
        return email

    def validate_phone(self, phone):
        pattern = re.compile(
            r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))")
        check = pattern.search(phone)
        if check is None:
            raise serializers.ValidationError("Phone number is not valid!")
        return phone

    def validate_password(self, raw: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        password = make_password(raw)
        return password


# custom my token obtain pair
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        # token['nickname'] = user.nickname
        # Add more custom fields from your custom user model, If you have a custom user model.
        # ...

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['email'] = self.user.email

        return data
