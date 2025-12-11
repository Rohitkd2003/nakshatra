from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="NAKSHATRA HEALTH API",
      default_version='v1',
      description="API documentation for Nakshatra Health project",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/auth/", include("auth_app.urls")),
    path("api/patients/", include("patients.urls")),
    path("api/consultations/", include("consultations.urls")),
    path("api/nutrition/", include("nutrition.urls")),
    path("api/fitness/", include("fitness.urls")),
    path("api/meditation/", include("meditation.urls")),
    path("api/metrics/", include("metrics.urls")),
    path("api/resources/", include("resources.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/community/", include("community.urls")),
    path("api/adminpanel/", include("adminpanel.urls")),
    path("api/health/", include("health.urls")),
    path("api/habits/", include("habits.urls")),


    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
