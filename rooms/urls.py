from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('<int:pk>/', views.room_detail, name='room_detail'),
    path('neu/', views.room_create, name='room_create'),
    path('<int:pk>/bearbeiten/', views.room_update, name='room_update'),
    path('<int:pk>/loeschen/', views.room_delete, name='room_delete'),
]
