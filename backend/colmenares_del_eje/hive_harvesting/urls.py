from django.urls import path
from . import views

urlpatterns = [
    path('hive-harvesting/<int:pk>/', views.hive_harvesting_view.as_view(), name='hive_harvesting'),
    path('edit-hive-harvesting/<int:pk>/', views.edit_hive_harvesting_view.as_view(), name='edit_hive_harvesting'),
    path('list-hive-harvesting/', views.list_hive_harvesting_view.as_view(), name='list_hive_harvesting'),
]