from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import PatientConfig, HealthTemplate, VitalRecord
from .serializers import (
    PatientConfigSerializer,
    TemplateSerializer,
    VitalRecordSerializer,
    PostSerializer,
    CommentSerializer,
    ConsultationSerializer,
    FitnessPlanSerializer,
    WorkoutLogSerializer,
    HabitTemplateSerializer,
    HabitSerializer,
    HabitLogSerializer,
    VitalTypeSerializer,
    VitalLogSerializer,
    MeditationPlanSerializer,
    MeditationSessionSerializer,
    HealthMetricSerializer,
    MealSerializer,
    MealLogSerializer,
    CalorieEntrySerializer,
)
from .permissions import IsAdmin
from community.models import Post, Comment
from consultations.models import Consultation
from fitness.models import FitnessPlan, WorkoutLog
from habits.models import HabitTemplate, Habit, HabitLog
from health.models import VitalType, VitalLog
from meditation.models import MeditationPlan, MeditationSession
from metrics.models import HealthMetric
from nutrition.models import Meal, MealLog, CalorieEntry



class PatientMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "success": True,
            "data": {
                "email": request.user.email,
                "name": request.user.full_name,
                "phone": request.user.phone,
                "role": request.user.role,
            }
        })


class TemplateListView(APIView):
    def get(self, request):
        templates = HealthTemplate.objects.all()
        serializer = TemplateSerializer(templates, many=True)
        return Response({"success": True, "data": serializer.data})


class PatientConfigView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        config, created = PatientConfig.objects.get_or_create(user=request.user)
        serializer = PatientConfigSerializer(config)
        return Response({"success": True, "data": serializer.data})

    @swagger_auto_schema(request_body=PatientConfigSerializer)
    def put(self, request):
        if request.user.role != "Admin":
            return Response({"error": "Only admin can update configs"}, status=403)

        user_id = request.query_params.get("user_id")  
        if not user_id:
            return Response({"error": "user_id is required"}, status=400)

        try:
            config = PatientConfig.objects.get(user_id=user_id)
        except PatientConfig.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)

        serializer = PatientConfigSerializer(config, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data})
        return Response(serializer.errors, status=400)


class VitalsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        vitals = VitalRecord.objects.filter(user=request.user)
        serializer = VitalRecordSerializer(vitals, many=True)
        return Response({"success": True, "data": serializer.data})

    @swagger_auto_schema(request_body=VitalRecordSerializer)
    def post(self, request):
        serializer = VitalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"success": True, "message": "Vital logged"})
        return Response(serializer.errors, status=400)


class PatientDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        posts = Post.objects.filter(user=user)
        comments = Comment.objects.filter(user=user)
        consultations = Consultation.objects.filter(patient=user)
        fitness_plans = FitnessPlan.objects.all()
        workout_logs = WorkoutLog.objects.filter(patient=user)
        habit_templates = HabitTemplate.objects.all()
        habits = Habit.objects.filter(user=user)
        habit_logs = HabitLog.objects.filter(habit__user=user)
        vital_types = VitalType.objects.all()
        vital_logs = VitalLog.objects.filter(user=user)
        meditation_plans = MeditationPlan.objects.all()
        meditation_sessions = MeditationSession.objects.filter(patient=user)
        health_metrics = HealthMetric.objects.filter(patient=user)
        meals = Meal.objects.all()
        meal_logs = MealLog.objects.filter(patient=user)
        calorie_entries = CalorieEntry.objects.filter(patient=user)

        data = {
            "community": {
                "posts": PostSerializer(posts, many=True).data,
                "comments": CommentSerializer(comments, many=True).data,
            },
            "consultations": {
                "consultations": ConsultationSerializer(consultations, many=True).data,
            },
            "fitness": {
                "fitness_plans": FitnessPlanSerializer(fitness_plans, many=True).data,
                "workout_logs": WorkoutLogSerializer(workout_logs, many=True).data,
            },
            "habits": {
                "habit_templates": HabitTemplateSerializer(habit_templates, many=True).data,
                "habits": HabitSerializer(habits, many=True).data,
                "habit_logs": HabitLogSerializer(habit_logs, many=True).data,
            },
            "health": {
                "vital_types": VitalTypeSerializer(vital_types, many=True).data,
                "vital_logs": VitalLogSerializer(vital_logs, many=True).data,
            },
            "meditation": {
                "meditation_plans": MeditationPlanSerializer(meditation_plans, many=True).data,
                "meditation_sessions": MeditationSessionSerializer(meditation_sessions, many=True).data,
            },
            "metrics": {
                "health_metrics": HealthMetricSerializer(health_metrics, many=True).data,
            },
            "nutrition": {
                "meals": MealSerializer(meals, many=True).data,
                "meal_logs": MealLogSerializer(meal_logs, many=True).data,
                "calorie_entries": CalorieEntrySerializer(calorie_entries, many=True).data,
            },
        }

        return Response({"success": True, "data": data})

