from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/servicelist/', ServiceAPIList.as_view(), name='service' ),
    path('api/v1/servicelist/<int:pk>/', ServiceAPIUpdate.as_view(), name='service' ),
    path('api/v1/servicedetail/<int:pk>/', ServiceAPIDetailView.as_view(), name='service' ),
    
]