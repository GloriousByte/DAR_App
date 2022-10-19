from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Citizen)
admin.site.register(Property)
admin.site.register(Receipt)
admin.site.register(Tag)