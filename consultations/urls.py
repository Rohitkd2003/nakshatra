from django.urls import path
from .views import (
    ConsultationListView,
    ConsultationDetailView,
    ConsultationCreateView,
    ConsultationStatusUpdateView,
)

urlpatterns = [
    path("", ConsultationListView.as_view()),
    path("<int:id>", ConsultationDetailView.as_view()),
    path("create", ConsultationCreateView.as_view()),
    path("<int:id>/status", ConsultationStatusUpdateView.as_view()),
]
