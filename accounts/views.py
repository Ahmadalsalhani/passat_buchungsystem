from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    """Login View"""
    if request.user.is_authenticated:
        return redirect('bookings:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Willkommen zurück, {user.username}!')
            return redirect('bookings:dashboard')
        else:
            messages.error(request, 'Ungültige Anmeldedaten.')
    
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    """Logout View"""
    logout(request)
    messages.info(request, 'Sie wurden erfolgreich abgemeldet.')
    return redirect('accounts:login')
