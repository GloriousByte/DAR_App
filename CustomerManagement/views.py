from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from .forms import OrderForm
from .filters import ReceiptFilter


def home(request):
    receipts = Receipt.objects.all()
    citizens = Citizen.objects.all()

    total_citizens = citizens.count()

    total_receipts = receipts.count()
    issued = receipts.filter(status='Issued').count()
    pending = receipts.filter(status='Pending').count()

    context = {'receipts': receipts, 'citizens': citizens,
               'total_receipts': total_receipts, 'issued': issued,
               'pending': pending}

    return render(request, 'CustomerManagement/dashboard.html', context)


def propertys(request):
    propertys = Property.objects.all()

    return render(request, 'CustomerManagement/products.html', {'propertys': propertys})


def citizen(request, pk_test):
    citizen = Citizen.objects.get(id=pk_test)

    receipts = citizen.receipt_set.all()
    receipt_count = receipts.count()

    myFilter = ReceiptFilter(request.GET, queryset=receipts)
    receipts = myFilter.qs

    context = {'citizen': citizen, 'receipts': receipts, 'receipt_count': receipt_count,
               'myFilter': myFilter}
    return render(request, 'CustomerManagement/customer.html', context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Citizen, Receipt, fields=('property', 'status'), extra=10)
    citizen = Citizen.objects.get(id=pk)
    formset = OrderFormSet(queryset=Receipt.objects.none(), instance=citizen)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=citizen)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': formset}
    return render(request, 'CustomerManagement/order_form.html', context)


def updateOrder(request, pk):
    order = Receipt.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'CustomerManagement/order_form.html', context)


def deleteOrder(request, pk):
    order = Receipt.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'CustomerManagement/delete.html', context)
