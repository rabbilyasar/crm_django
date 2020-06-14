from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from accounts.models import *


def home(request):
    orders = Order.objects.all()
    last_5_orders = orders.order_by('-id')[:5]
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count
    pending = orders.filter(status='Pending').count

    context = {'orders': orders, 'customers': customers,
               'last_5_orders': last_5_orders, 'total_customers': total_customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customers(request, pk):
    customer = get_object_or_404(Customer, id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer,
               'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customers.html', context)
