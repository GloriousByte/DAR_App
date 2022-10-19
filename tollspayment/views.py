from django.shortcuts import render, redirect
from django.urls import reverse
import stripe
from django.http import JsonResponse

stripe.api_key = "sk_test_GWXhmDhhUYhSqPkfItT4yvYJ00sn5dzkMq"


# Create your views here.

def index(request):
    return render(request, 'tollspayment/index2.html')


def charge2(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount2 = int(request.POST['amount2'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount2 * 100,
            currency='usd',
            description='Government Facilities tolls'
        )

    return redirect(reverse('success2', args=[amount2]))


def successMsg2(request, args):
    amount2 = args
    return render(request, 'tollspayment/success2.html', {'amount2': amount2})


def index3(request):
    return render(request, 'tollspayment/index3.html')


def charge3(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount3 = int(request.POST['amount3'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount3 * 100,
            currency='usd',
            description='Donations'
        )

    return redirect(reverse('success3', args=[amount3]))


def successMsg3(request, args):
    amount3 = args
    return render(request, 'tollspayment/success3.html', {'amount3': amount3})
