"""
URL configuration for passat_buchungssystem project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('bookings:dashboard'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('bookings.urls')),
    path('kunden/', include('customers.urls')),
    path('raeume/', include('rooms.urls')),
    path('rechnungen/', include('invoices.urls')),
]

# Media files (development only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
