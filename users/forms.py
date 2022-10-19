from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Bankaccount


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Street", required=True)
    last_name = forms.CharField(label="house", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
            super(UserRegisterForm, self).__init__(*args, **kwargs)


class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'street', 'house_number', 'amount_owed']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

