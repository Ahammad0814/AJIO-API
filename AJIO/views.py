from django.shortcuts import render
from django.http import JsonResponse
from . serializer import MenSerializer,WomenSerializer,KidsSerializer,LoginSerializer,OrdersSerializer
from . models import MensData,WomensData,KidsData,LoginData,OrdersData
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED
from rest_framework import status

# Create your views here.

@api_view(['GET','POST','DELETE'])
def Men_Data(request):
    if request.method == 'GET':
        Item_Data = MensData.objects.all()
        serializer = MenSerializer(Item_Data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        Data = MenSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status= HTTP_201_CREATED)

    
@api_view(['GET','POST','DELETE'])
def Women_Data(request):
    if request.method == 'GET':
        Item_Data = WomensData.objects.all()
        serializer = WomenSerializer(Item_Data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        Data = WomenSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status= HTTP_201_CREATED)
    
@api_view(['GET','POST','DELETE'])
def Kids_Data(request):
    if request.method == 'GET':
        Item_Data = KidsData.objects.all()
        serializer = KidsSerializer(Item_Data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        Data = KidsSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status= HTTP_201_CREATED)
    
@api_view(['GET','POST','DELETE'])
def Login_Data(request):
    if request.method == 'GET':
        Item_Data = LoginData.objects.all()
        serializer = LoginSerializer(Item_Data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        Data = LoginSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status= HTTP_201_CREATED)
    
@api_view(['GET','POST','DELETE'])
def Orders_Data(request):
    if request.method == 'GET':
        Item_Data = OrdersData.objects.all()
        serializer = OrdersSerializer(Item_Data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        Data = OrdersSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status= HTTP_201_CREATED)