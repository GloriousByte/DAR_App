from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('propertys/', views.propertys, name='propertys'),
    path('citizen/<str:pk_test>/', views.citizen, name='citizen'),

 path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),



]