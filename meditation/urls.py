from django.urls import path
from .views import MeditationSessionCreateView, MeditationSessionListView, PlanListView

urlpatterns = [
    path('plans/', PlanListView.as_view(), name='plans'),
    path('sessions/', MeditationSessionCreateView.as_view(), name='session-create'),
    path('sessions/list/', MeditationSessionListView.as_view(), name='session-list'),
]
