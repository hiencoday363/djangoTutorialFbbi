from django.urls import path

from apps.EventView.views import list_event

# prefix: view-event/
urlpatterns = [
    path(r'', list_event, name='view_event'),
]
