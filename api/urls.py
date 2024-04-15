from django.contrib import admin
from django.urls import path,include
from .views import IterationView,ControllerView
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'iteration', IterationView)
routers.register(r'loanController', ControllerView)

urlpatterns = [
    path('api/', include(routers.urls)),
    

]


