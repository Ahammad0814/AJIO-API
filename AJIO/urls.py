from django.urls import path
from . import views

urlpatterns = [
    path('men/',views.Men_Data,name='Men'),
    path('women/',views.Women_Data,name='Women'),
    path('kids/',views.Kids_Data,name='Kids'),
    path('login/',views.Login_Data,name='Login'),
    path('orders/',views.Orders_Data,name='Orders'),
]
