from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework_simplejwt.tokens import RefreshToken


class MyOauth(View):
    template_name = 'oauth/index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CheckLogin(View):
    template_name = 'oauth/login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            token = RefreshToken.for_user(user)
            return redirect(f'http://localhost:8000/?token={token.access_token}')
        return render(request, self.template_name)


class Login(View):
    template_name = 'oauth/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('http://localhost:8000/?token=hiencoday')

        return render(request, self.template_name)

#
# class FacebookSocialAuthView(GenericAPIView):
#     serializer_class = FacebookSocialAuthSerializer
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         """
#         POST with "auth_token"
#         Send an access token as from facebook to get user information
#         """
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data = ((serializer.validated_data)['auth_token'])
#         return Response(data, status=status.HTTP_200_OK)
