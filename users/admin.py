from .models import Profile
from .models import Bankaccount
from .models import CreditCardPayments
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton


admin.site.register(Profile)
admin.site.register(Bankaccount)
admin.site.register(CreditCardPayments)