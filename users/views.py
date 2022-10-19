from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from Advertisement.models import Post
from .models import CreditCardPayments
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.http import JsonResponse
from django.urls import reverse

import stripe

stripe.api_key = "sk_test_GWXhmDhhUYhSqPkfItT4yvYJ00sn5dzkMq"


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html')


@login_required
def ratesprofile(request):
    return render(request, 'users/ratesprofile.html', )


@login_required
def tollsprofile(request):
    return render(request, 'users/tollsprofile.html', )


@login_required
def payoption(request):
    return render(request, 'users/payoption.html', )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = CreditCardPayments
    template_name = 'users/Creditcardinfo.html'
    fields = ['Account_Name', 'Bank_UC', 'Card_Number', 'CUL']

    def form_valid(self, form):
        form.instance.payer = self.request.user
        return super().form_valid(form)


class CreditCardDetailView(DetailView):
    model = CreditCardPayments
    template_name = 'users/Creditdetail.html'


def test(request):
    return render(request, 'users/intropage.html')


@login_required
def visacardpay(request):
    return render(request, 'users/visacardpay.html')


def charge(request):
    return render(request, 'users/success.html')
