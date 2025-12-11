from django.urls import path
from .views import HabitTemplateView, HabitListCreateView, HabitLogView

urlpatterns = [
    path("habit-templates/", HabitTemplateView.as_view()),
    path("habits/", HabitListCreateView.as_view()),
    path("habit-logs/", HabitLogView.as_view()),
]
