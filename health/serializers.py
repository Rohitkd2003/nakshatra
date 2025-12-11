from rest_framework import serializers
from .models import VitalType, VitalLog

class VitalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalType
        fields = "__all__"


class VitalLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalLog
        fields = "__all__"
