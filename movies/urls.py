from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Movie Api",
        default_version="v1",
        description="Api de peliculas",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movies/", include("movie.urls")),
    path("users/", include("user.urls")),
    path("rents/", include("rent.urls")),
    path(
        "swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-docs"
    ),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
