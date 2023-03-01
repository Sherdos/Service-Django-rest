from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import*
from .serializers import*


# Create your views here.


# class ServiceList(generics.ListAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer

class ServiceList(APIView):
    def get(self, request):
        lst = Service.objects.all().values()
        return Response({'service':list(lst)})
    
    def post(self,request):
        service_new = Service.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            price=request.data['price'],
            end=request.data['end'],
        )
        return Response({'post':model_to_dict(service_new)})
        
        
