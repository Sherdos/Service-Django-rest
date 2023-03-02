import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *



class ServiceSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=255)
    description = serializers.CharField()
    create = serializers.DateField(read_only=True)
    price = serializers.IntegerField()
    start = serializers.DateTimeField(read_only=True)
    end = serializers.DateTimeField()
    
    
# def encode():
#     model = ServiceModel('Python','desription: Python Это очень легко')
#     model_sr = ServiceSerializer(model)
#     json = JSONRenderer().render(model_sr.data)
    
# def decode():
#     stream=io.BytesIO(b'{"title":"Python", "description":" Python Hello" }')
#     data = JSONParser().parse(stream)
#     serializer = ServiceSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
    