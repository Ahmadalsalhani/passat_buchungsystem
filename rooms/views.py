from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Room
from .forms import RoomForm

@login_required
def room_list(request):
    """Liste aller Räume"""
    search_query = request.GET.get('search', '')
    rooms = Room.objects.all()
    
    if search_query:
        rooms = rooms.filter(
            Q(raumnummer__icontains=search_query) |
            Q(raumname__icontains=search_query) |
            Q(raumtyp__icontains=search_query)
        )
    
    context = {
        'rooms': rooms,
        'search_query': search_query,
    }
    return render(request, 'rooms/room_list.html', context)

@login_required
def room_detail(request, pk):
    """Detailansicht eines Raums"""
    room = get_object_or_404(Room, pk=pk)
    context = {'room': room}
    return render(request, 'rooms/room_detail.html', context)

@login_required
def room_create(request):
    """Neuen Raum anlegen"""
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            messages.success(request, f'Raum {room.raumnummer} wurde erfolgreich erstellt.')
            return redirect('rooms:room_detail', pk=room.pk)
    else:
        form = RoomForm()
    
    context = {'form': form}
    return render(request, 'rooms/room_form.html', context)

@login_required
def room_update(request, pk):
    """Raum bearbeiten"""
    room = get_object_or_404(Room, pk=pk)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room = form.save()
            messages.success(request, f'Raum {room.raumnummer} wurde erfolgreich aktualisiert.')
            return redirect('rooms:room_detail', pk=room.pk)
    else:
        form = RoomForm(instance=room)
    
    context = {'form': form, 'room': room}
    return render(request, 'rooms/room_form.html', context)

@login_required
def room_delete(request, pk):
    """Raum löschen"""
    room = get_object_or_404(Room, pk=pk)
    
    if request.method == 'POST':
        number = room.raumnummer
        room.delete()
        messages.success(request, f'Raum {number} wurde erfolgreich gelöscht.')
        return redirect('rooms:room_list')
    
    context = {'room': room}
    return render(request, 'rooms/room_confirm_delete.html', context)
