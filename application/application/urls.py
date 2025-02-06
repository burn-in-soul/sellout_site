"""
URL configuration for application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from application.application.schema import schema_view

urlpatterns = [
    path('sellout/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('sellout/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('sellout/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('sellout/admin/', admin.site.urls),
    path('sellout/api/concerts/', include('application.concerts.urls')),
]
