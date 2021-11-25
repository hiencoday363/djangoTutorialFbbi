from django.urls import path
from .views import *

app_name = 'event_app'

urlpatterns = [
    path('event-viewset/', EventViewSet.as_view()),  # use generics.ListAPIView

    path('event/', EventApiView.as_view()),
    path('event/<int:pk>/', DetailEventApiView.as_view()),

    # ticket
    path('tickets/all/', TicketListApiView.as_view()),
    path('tickets/<int:pk>/drawings/', TicketApiView.as_view()),

    path('tickets/all-check/', TicketCheckApiView.as_view()),
    path('perform/all/', PerformanceListApiView.as_view()),
]



