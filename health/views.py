from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import VitalType, VitalLog
from .serializers import VitalTypeSerializer, VitalLogSerializer


class VitalTypeListView(APIView):
    def get(self, request):
        vitals = VitalType.objects.all()
        serializer = VitalTypeSerializer(vitals, many=True)
        return Response(serializer.data)


class VitalLogListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logs = VitalLog.objects.filter(user=request.user)
        serializer = VitalLogSerializer(logs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VitalLogSerializer)
    def post(self, request):
        data = request.data.copy()
        data["user"] = request.user.id
        serializer = VitalLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
