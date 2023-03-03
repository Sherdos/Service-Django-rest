from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/servicelist/', ServiceList.as_view(), name='service' ),
    path('api/v1/servicelist/<int:pk>/', ServiceList.as_view(), name='service' ),
]