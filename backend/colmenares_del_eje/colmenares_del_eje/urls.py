"""
URL configuration for colmenares_del_eje project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('beehive/', include('hive_management.urls')),
    path('weather/', include('weather_conditions.urls')),
    path('monitoring/', include('beehive_monitoring.urls')),
    path('harvesting/', include('hive_harvesting.urls')),
    path('beekeepers/', include('beekeeper_management.urls')),
    path('location/', include('location.urls')),
]
