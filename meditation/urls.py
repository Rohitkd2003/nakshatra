from django.urls import path
from .views import (
    MeditationSessionCreateView,
    MeditationSessionListView,
    MeditationSessionDetailView,
    PlanListView,
    PlanDetailView,
)

urlpatterns = [
    path('plans/', PlanListView.as_view(), name='plans'),
    path('plans/<int:pk>/', PlanDetailView.as_view(), name='plan-detail'),
    path('sessions/', MeditationSessionCreateView.as_view(), name='session-create'),
    path('sessions/list/', MeditationSessionListView.as_view(), name='session-list'),
    path('sessions/<int:pk>/', MeditationSessionDetailView.as_view(), name='session-detail'),
]
