from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Customer
from .forms import CustomerForm

@login_required
def customer_list(request):
    """Liste aller Kunden mit Suchfunktion"""
    search_query = request.GET.get('search', '')
    customers = Customer.objects.all()
    
    if search_query:
        customers = customers.filter(
            Q(vorname__icontains=search_query) |
            Q(nachname__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(telefon__icontains=search_query)
        )
    
    context = {
        'customers': customers,
        'search_query': search_query,
    }
    return render(request, 'customers/customer_list.html', context)

@login_required
def customer_detail(request, pk):
    """Detailansicht eines Kunden"""
    customer = get_object_or_404(Customer, pk=pk)
    context = {'customer': customer}
    return render(request, 'customers/customer_detail.html', context)

@login_required
def customer_create(request):
    """Neuen Kunden anlegen"""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            messages.success(request, f'Kunde {customer.get_full_name()} wurde erfolgreich erstellt.')
            return redirect('customers:customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    
    context = {'form': form}
    return render(request, 'customers/customer_form.html', context)

@login_required
def customer_update(request, pk):
    """Kunden bearbeiten"""
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save()
            messages.success(request, f'Kunde {customer.get_full_name()} wurde erfolgreich aktualisiert.')
            return redirect('customers:customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    
    context = {'form': form, 'customer': customer}
    return render(request, 'customers/customer_form.html', context)

@login_required
def customer_delete(request, pk):
    """Kunden löschen"""
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'POST':
        name = customer.get_full_name()
        customer.delete()
        messages.success(request, f'Kunde {name} wurde erfolgreich gelöscht.')
        return redirect('customers:customer_list')
    
    context = {'customer': customer}
    return render(request, 'customers/customer_confirm_delete.html', context)
