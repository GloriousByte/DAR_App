
from django.contrib import admin
from .models import Snippet
from users.models import Bankaccount
from users.models import CreditCardPayments

admin.site.site_header = 'Oforikurom DARS'

admin.site.register(Snippet)
admin.site.unregister(Bankaccount)
admin.site.unregister(CreditCardPayments)
admin.site.unregister(Snippet)