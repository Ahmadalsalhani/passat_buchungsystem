from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('liste/', views.booking_list, name='booking_list'),
    path('kalender/', views.calendar_overview, name='calendar_overview'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
    path('neu/', views.booking_create, name='booking_create'),
    path('<int:pk>/bearbeiten/', views.booking_update, name='booking_update'),
    path('<int:pk>/loeschen/', views.booking_delete, name='booking_delete'),
    # Autocomplete endpoints
    path('api/customers/autocomplete/', views.customer_autocomplete, name='customer_autocomplete'),
    path('api/rooms/autocomplete/', views.room_autocomplete, name='room_autocomplete'),
]
