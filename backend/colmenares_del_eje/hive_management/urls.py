from django.urls import path
from . import views

urlpatterns = [
    path('create-hive/', views.create_hive_view.as_view(), name='create_hive'),
    path('edit-hive/<int:pk>/', views.edit_hive_view.as_view(), name='edit_hive'),
    path('detail-hive/<int:pk>/', views.detail_hive_view.as_view(), name='detail_hive'),
    path('list-hives/', views.list_hives_view.as_view(), name='list_hives'),
    
]