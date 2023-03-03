import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *



class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=255)
    description = serializers.CharField()
    create = serializers.DateField(read_only=True)
    price = serializers.IntegerField()
    start = serializers.DateTimeField(read_only=True)
    end = serializers.DateTimeField()
    
    
    def create(self, validated_data):
        return Service.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title=validated_data.get('title', instance.title)
        instance.description=validated_data.get('description', instance.description)
        instance.price=validated_data.get('price', instance.price)
        instance.end=validated_data.get('end', instance.end)
        instance.save()
        return instance
    
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
    