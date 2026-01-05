from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('<int:pk>/', views.customer_detail, name='customer_detail'),
    path('neu/', views.customer_create, name='customer_create'),
    path('<int:pk>/bearbeiten/', views.customer_update, name='customer_update'),
    path('<int:pk>/loeschen/', views.customer_delete, name='customer_delete'),
]
