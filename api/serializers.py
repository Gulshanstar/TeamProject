from rest_framework import serializers
from .models import IterationModels, ControllerModels

class IterationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IterationModels
        fields = "__all__"


# # Create serializers for the activities
class ControllerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ControllerModels
        fields = "__all__"
