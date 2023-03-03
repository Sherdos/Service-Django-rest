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
        return Response(ServiceSerializer(s,many=True).data)
    
    def post(self,request):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'service':serializer.data}) 
        
        
    def put(self, request,*args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error":"Metod PUT not allowed"})
        try:
            instance = Service.objects.get(pk=pk)
        except:
            return Response({"error":"Object does not exists"})
        
        
        serializer = ServiceSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post':serializer.data})
        
    def delete(self, request,*args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error":"Metod DELETE not allowed"})
        try:
            instance = Service.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"error":"Object does not exists"})
        return Response({'post':'delete post '+str(pk)})
        
