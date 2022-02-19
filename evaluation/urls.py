"""evaluation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

# from facilities.urls import urlpatterns as facility_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from evaluation import settings

schema_view = get_schema_view(
        openapi.Info(
            title="Health Facilities API",
            default_version='v1',
            description="This API is provided by New York City Government Health Department",
            terms_of_service="https://www.google.com/polices/terms/",
            contact=openapi.Contact(email="hello@example.com"),
            license=openapi.License(name="BSD License"),

        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/v1/', include("facilities.urls")),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc/', cache_timeout=0, name='schema-redoc')),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
