from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from .models import Booking
from .forms import BookingForm
from customers.models import Customer

@login_required
def dashboard(request):
    """Dashboard mit Statistiken"""
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(status='ausstehend').count()
    confirmed_bookings = Booking.objects.filter(status='bestaetigt').count()
    total_customers = Customer.objects.count()
    
    recent_bookings = Booking.objects.all()[:5]
    
    context = {
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'confirmed_bookings': confirmed_bookings,
        'total_customers': total_customers,
        'recent_bookings': recent_bookings,
    }
    return render(request, 'bookings/dashboard.html', context)

@login_required
def booking_list(request):
    """Liste aller Buchungen"""
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    
    bookings = Booking.objects.select_related('kunde', 'raum').all()
    
    if search_query:
        bookings = bookings.filter(
            Q(kunde__vorname__icontains=search_query) |
            Q(kunde__nachname__icontains=search_query) |
            Q(raum__raumnummer__icontains=search_query) |
            Q(raum__raumname__icontains=search_query)
        )
    
    if status_filter:
        bookings = bookings.filter(status=status_filter)
    
    context = {
        'bookings': bookings,
        'search_query': search_query,
        'status_filter': status_filter,
        'status_choices': Booking.STATUS_CHOICES,
    }
    return render(request, 'bookings/booking_list.html', context)

@login_required
def booking_detail(request, pk):
    """Detailansicht einer Buchung"""
    booking = get_object_or_404(Booking.objects.select_related('kunde', 'raum'), pk=pk)
    context = {'booking': booking}
    return render(request, 'bookings/booking_detail.html', context)

@login_required
def booking_create(request):
    """Neue Buchung anlegen"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                booking = form.save()
                messages.success(request, f'Buchung #{booking.pk} wurde erfolgreich erstellt.')
                return redirect('bookings:booking_detail', pk=booking.pk)
            except Exception as e:
                messages.error(request, f'Fehler beim Erstellen der Buchung: {str(e)}')
    else:
        form = BookingForm()
    
    context = {'form': form}
    return render(request, 'bookings/booking_form.html', context)

@login_required
def booking_update(request, pk):
    """Buchung bearbeiten"""
    booking = get_object_or_404(Booking, pk=pk)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            try:
                booking = form.save()
                messages.success(request, f'Buchung #{booking.pk} wurde erfolgreich aktualisiert.')
                return redirect('bookings:booking_detail', pk=booking.pk)
            except Exception as e:
                messages.error(request, f'Fehler beim Aktualisieren der Buchung: {str(e)}')
    else:
        form = BookingForm(instance=booking)
    
    context = {'form': form, 'booking': booking}
    return render(request, 'bookings/booking_form.html', context)

@login_required
def booking_delete(request, pk):
    """Buchung löschen"""
    booking = get_object_or_404(Booking, pk=pk)
    
    if request.method == 'POST':
        booking_id = booking.pk
        booking.delete()
        messages.success(request, f'Buchung #{booking_id} wurde erfolgreich gelöscht.')
        return redirect('bookings:booking_list')
    
    context = {'booking': booking}
    return render(request, 'bookings/booking_confirm_delete.html', context)
