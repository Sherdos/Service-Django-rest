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
        s = Service.objects.all()
        return Response({'service':ServiceSerializer(s,many=True).data})
    
    def post(self,request):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service_new = Service.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            price=request.data['price'],
            end=request.data['end'],
        )
        return Response({'service':ServiceSerializer(service_new).data})
        
        
