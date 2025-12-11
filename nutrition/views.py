from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import MealPlan
from .serializers import MealPlanAddFoodSerializer

from .models import Meal, MealLog, CalorieEntry
from .serializers import (
    MealListSerializer,
    MealDetailSerializer,
    MealLogCreateSerializer,
    MealLogSerializer,
    CalorieEntrySerializer
)

# -------------------
# Meals
# -------------------

# List + Create meals (GET list / POST create)
class MealListView(generics.ListCreateAPIView):
    queryset = Meal.objects.all().order_by('-created_at')
    serializer_class = MealListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['condition']
    search_fields = ['name', 'description']
    ordering_fields = ['calories', 'created_at']
    permission_classes = [permissions.AllowAny]  # Public endpoint
    pagination_class = PageNumberPagination

# Retrieve single meal by ID
class MealDetailView(generics.RetrieveAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

# -------------------
# Meal Logs (Patient only)
# -------------------

# Create meal log (POST)
class MealLogCreateView(generics.CreateAPIView):
    serializer_class = MealLogCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

# List meal logs (GET) with optional date filters
class MealLogListView(generics.ListAPIView):
    serializer_class = MealLogSerializer
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
        qs = MealLog.objects.filter(patient=user).order_by('-logged_at')

        # Date filters
        date = self.request.query_params.get('date')
        if date:
            qs = qs.filter(date=date)

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            qs = qs.filter(date__range=[start_date, end_date])

        return qs

# -------------------
# Calorie Entry
# -------------------

class CalorieEntryCreateView(generics.CreateAPIView):
    serializer_class = CalorieEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}

from rest_framework import generics, permissions
from .models import MealPlan, Meal, MealPlanItem
from .serializers import MealPlanItemSerializer
from .serializers import MealPlanAddFoodSerializer

class MealPlanAddFoodView(generics.CreateAPIView):
    queryset = MealPlanItem.objects.all()
    serializer_class = MealPlanItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        mealplan_id = self.kwargs.get('pk')
        mealplan = MealPlan.objects.get(id=mealplan_id)
        serializer.save(mealplan=mealplan)
