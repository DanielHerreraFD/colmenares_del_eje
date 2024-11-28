from django.urls import path
from . import views

urlpatterns = [
    path('beehive-weather/<int:pk>/', views.beehive_weather_view.as_view(), name='beehive_weather'),
]