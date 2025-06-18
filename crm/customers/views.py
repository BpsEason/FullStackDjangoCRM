from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer

@login_required
def customer_list(request):
    customers = Customer.objects.filter(created_by=request.user)
    return render(request, 'customers/customer_list.html', {'customers': customers})

@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk, created_by=request.user)
    return render(request, 'customers/customer_detail.html', {'customer': customer})