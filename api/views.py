from django.shortcuts import render
from rest_framework import viewsets
from .models import IterationModels,ControllerModels
from .serializers import IterationSerializer,ControllerSerializer
from temporalio.client import Client

# Create your views here.
class IterationView(viewsets.ModelViewSet):
    queryset = IterationModels.objects.all()
    serializer_class = IterationSerializer

class ControllerView(viewsets.ModelViewSet):
    queryset = ControllerModels.objects.all()
    serializer_class = ControllerSerializer

    
