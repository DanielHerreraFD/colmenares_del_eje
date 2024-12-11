from django.urls import path
from . import views

urlpatterns = [     
    path('hive-location/<int:pk>/', views.hive_location_view.as_view(), name='hive_location'),
]   