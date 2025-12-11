from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import HabitTemplate, Habit, HabitLog
from .serializers import HabitTemplateSerializer, HabitSerializer, HabitLogSerializer


class HabitTemplateView(APIView):
    def get(self, request):
        templates = HabitTemplate.objects.all()
        serializer = HabitTemplateSerializer(templates, many=True)
        return Response(serializer.data)


class HabitListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=HabitSerializer)
    def post(self, request):
        data = request.data.copy()
        data["user"] = request.user.id
        serializer = HabitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class HabitLogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logs = HabitLog.objects.filter(habit__user=request.user)
        serializer = HabitLogSerializer(logs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=HabitLogSerializer)
    def post(self, request):
        serializer = HabitLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
