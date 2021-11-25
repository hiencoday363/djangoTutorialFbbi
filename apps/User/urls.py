from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import *

# prefix: user/

urlpatterns = [
    #path('test/', hello),  # test hash pass (but never use )
    path('all/', RegisterView.as_view()),
    path('detail/<int:id>', DetailUserApiView.as_view()),

    # for api to get token and refresh (to check)
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
