from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
# from django.conf import settings
# from django.conf.urls.static import static

# add rest swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# custom text from admin page
admin.site.site_header = "HienCoDay"
admin.site.site_title = "HienCoDay Title"
admin.site.index_title = "HienCoDay SubTitle"

schema_view = get_schema_view(
    openapi.Info(
        title="Hiencoday",
        default_version='v1',
        description="Display all route",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('apps.oauth.urls')),

    path('url/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('view-event/', include('apps.EventView.urls')),
    path('user/', include('apps.User.urls')),
    path('api/v1/', include('apps.Event.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls), prefix_default_language=False
)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
