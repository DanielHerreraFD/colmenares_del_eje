from django.urls import path
from . import views

urlpatterns = [
    path('create-beekeeper/', views.create_beekeeper_view.as_view(), name='create_beekeeper'),
    path('edit-beekeeper/<int:pk>/', views.edit_beekeeper_view.as_view(), name='edit_beekeeper'),
    path('detail-beekeeper/<int:pk>/', views.detail_beekeeper_view.as_view(), name='detail_beekeeper'),
    path('list-beekeepers/', views.list_beekeepers_view.as_view(), name='list_beekeepers'),
]