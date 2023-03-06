from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/servicelist/', ServiceAPIList.as_view(), name='service' ),
    path('api/v1/servicelist/<int:pk>/', ServiceAPIList.as_view(), name='service' ),
]