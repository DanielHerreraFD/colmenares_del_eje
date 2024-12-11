from django.urls import path
from . import views

urlpatterns = [
    path('beehive-monitoring/<int:colmena_id>/', views.beehive_monitoring_view.as_view(), name='beehive_monitoring'),
    path('edit-beehive-monitoring/<int:pk>/', views.edit_beehive_monitoring_view.as_view(), name='edit_beehive_monitoring'),
    path('list-beehive-monitoring/', views.list_beehive_monitoring_view.as_view(), name='list_beehive_monitoring'),
]