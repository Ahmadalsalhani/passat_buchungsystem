from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('neu/', views.invoice_create, name='invoice_create'),
    path('<int:pk>/bearbeiten/', views.invoice_update, name='invoice_update'),
    path('<int:pk>/loeschen/', views.invoice_delete, name='invoice_delete'),
    path('<int:pk>/pdf/', views.invoice_pdf, name='invoice_pdf'),
]
