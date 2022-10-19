from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index2"),
    path('charge2/', views.charge2, name="charge2"),
    path('success2/<str:args>/', views.successMsg2, name="success2"),
    path('index3', views.index3, name="index3"),
    path('charge3/', views.charge3, name="charge3"),
    path('success3/<str:args>/', views.successMsg3, name="success3"),
]