from django.urls import path
from . import views
from .views import (

    PostCreateView,
    CreditCardDetailView,

)

urlpatterns = [
    path('', views.test, name='test'),
    path('viewpropertybill', views.ratesprofile, name='ratesprofile'),
    path('visacardpay', views.visacardpay, name='visacardpay'),
    path('tollsprofile', views.tollsprofile, name='tollsprofile'),
    path('payoption', views.payoption, name='payoption'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', CreditCardDetailView.as_view(), name='creditcard-detail'),
    path('charge/', views.charge, name="receipttemp"),
]