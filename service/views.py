from rest_framework import generics
from .serializers import*


# Create your views here.


class ServiceAPIList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
        
        

class ServiceAPIUpdate(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class=ServiceSerializer

class ServiceAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer