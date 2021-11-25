from django.urls import path, include
from django.contrib.auth import views as auth_views

from apps.oauth.views import MyOauth, Login, CheckLogin#, FacebookSocialAuthView

# prefix = oauth/

urlpatterns = [
    # path("access-fb/", FacebookSocialAuthView.as_view(), name="access_fb"),
    
    path('', MyOauth.as_view(), name='index_oauth'),
    path('check/', CheckLogin.as_view(), name='check_login'),

    path("login/", Login.as_view(), name="login"),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
]


