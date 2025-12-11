from rest_framework import serializers
from .models import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    patient_email = serializers.CharField(source="patient.email", read_only=True)
    doctor_email = serializers.CharField(source="doctor.email", read_only=True)

    class Meta:
        model = Consultation
        fields = "__all__"
        read_only_fields = ["status"]


# Serializer for updating only the status of a consultation
class ConsultationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'status']  # फक्त status update साठी
