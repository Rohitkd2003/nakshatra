from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import FitnessPlan, WorkoutLog
from .serializers import (
    FitnessPlanListSerializer, FitnessPlanDetailSerializer,
    WorkoutLogCreateSerializer, WorkoutLogSerializer
)

class FitnessPlanListView(generics.ListAPIView):
    queryset = FitnessPlan.objects.all().order_by('-created_at')
    serializer_class = FitnessPlanListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['plan_type','intensity']
    search_fields = ['name','description']
    ordering_fields = ['duration_minutes','created_at']
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination

class FitnessPlanDetailView(generics.RetrieveAPIView):
    queryset = FitnessPlan.objects.all()
    serializer_class = FitnessPlanDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class WorkoutLogCreateView(generics.CreateAPIView):
    serializer_class = WorkoutLogCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}

class WorkoutLogListView(generics.ListAPIView):
    serializer_class = WorkoutLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("date", openapi.IN_QUERY, type=openapi.TYPE_STRING, format="date", required=False),
            openapi.Parameter("start_date", openapi.IN_QUERY, type=openapi.TYPE_STRING, format="date", required=False),
            openapi.Parameter("end_date", openapi.IN_QUERY, type=openapi.TYPE_STRING, format="date", required=False),
        ]
    )
    def get_queryset(self):
        user = self.request.user
        qs = WorkoutLog.objects.filter(patient=user).order_by('-logged_at')
        # Optional date filter
        date = self.request.query_params.get('date')
        if date:
            qs = qs.filter(date=date)
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            qs = qs.filter(date__range=[start_date,end_date])
        return qs

from rest_framework import generics, permissions
from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseCreateView(generics.CreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]  # tumhi public karnya sathi AllowAny pan vapru shakta
