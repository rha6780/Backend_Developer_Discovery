"""developer_discover URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.http import JsonResponse

from rest_framework import permissions
from rest_framework.views import Response, APIView

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularYAMLAPIView,
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

# schema_view = get_schema_view(
#     openapi.Info(
#         title="development discovery",
#         default_version="",
#         description="API Docs",
#         terms_of_service="https://www.google.com/policies/terms/",
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )


class PingAPI(APIView):
    permission_classes = []

    def get(self, *args, **kwargs):
        return Response({"ping": "pong"})


spectacular = [
    path("docs/json", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path("docs/yaml", SpectacularYAMLAPIView.as_view(), name="schema"),
    # path('schema/user', SpectacularAPIView.as_view(), name='user_schema'),
    path("docs/swagger", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("docs/redoc", SpectacularRedocView.as_view(url_name="schema")),
]


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("api/v1/", include("apps.api.v1.urls")),
        path("ping", PingAPI.as_view(), name="ping"),
        path("", include("apps.pages.urls")),
        path("", include("django_nextjs.urls")),
        # path(r"swagger", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
        # path(r"redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc-v1"),
    ]
    + spectacular
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
