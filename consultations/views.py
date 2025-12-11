from django.shortcuts import render
from .serializers import ConsultationSerializer, ConsultationStatusSerializer

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Consultation
from .serializers import (
    ConsultationSerializer,
    ConsultationStatusSerializer
)
from .permissions import IsAdmin, IsDoctorOrAdmin


class ConsultationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == "Admin":
            consultations = Consultation.objects.all()
        elif request.user.role == "Doctor":
            consultations = Consultation.objects.filter(doctor=request.user)
        else:
            consultations = Consultation.objects.filter(patient=request.user)

        serializer = ConsultationSerializer(consultations, many=True)
        return Response({"success": True, "data": serializer.data})


class ConsultationDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            consultation = Consultation.objects.get(id=id)
        except Consultation.DoesNotExist:
            return Response({"error": "Not Found"}, status=404)

        # authorization
        if request.user.role == "Admin":
            pass
        elif request.user.role == "Doctor" and consultation.doctor_id != request.user.id:
            return Response({"error": "Forbidden"}, status=403)
        elif request.user.role == "Patient" and consultation.patient_id != request.user.id:
            return Response({"error": "Forbidden"}, status=403)

        serializer = ConsultationSerializer(consultation)
        return Response({"success": True, "data": serializer.data})


class ConsultationCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(request_body=ConsultationSerializer)
    def post(self, request):
        serializer = ConsultationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Consultation created",
                "data": serializer.data
            }, status=201)
        return Response(serializer.errors, status=400)


class ConsultationStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsDoctorOrAdmin]

    @swagger_auto_schema(request_body=ConsultationStatusSerializer)
    def patch(self, request, id):
        try:
            consultation = Consultation.objects.get(id=id)
        except Consultation.DoesNotExist:
            return Response({"error": "Not Found"}, status=404)

        serializer = ConsultationStatusSerializer(consultation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Status updated",
                "data": serializer.data
            })
        return Response(serializer.errors, status=400)
