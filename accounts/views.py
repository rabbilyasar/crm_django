from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from accounts.models import *
from accounts.forms import *


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


def createOrder(request):

    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    
    if request.method == "POST":
        order.delete()
        return redirect ('home')
    
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
