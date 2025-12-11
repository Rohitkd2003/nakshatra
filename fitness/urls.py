from django.urls import path
from .views import ExerciseCreateView 
from .views import (
    FitnessPlanListView, FitnessPlanDetailView,
    WorkoutLogCreateView, WorkoutLogListView
)

urlpatterns = [
    path("plans", FitnessPlanListView.as_view()),             # GET /fitness/plans
    path("plans/<int:id>", FitnessPlanDetailView.as_view()), # GET /fitness/plans/{id}
    path("workout-logs", WorkoutLogCreateView.as_view()),    # POST /fitness/workout-logs
    path("workout-logs/list", WorkoutLogListView.as_view()), # GET /fitness/workout-logs
    path('exercise/create', ExerciseCreateView.as_view(), name='exercise-create'),
    path('exercise/create/', ExerciseCreateView.as_view(), name='exercise-create'),


]
