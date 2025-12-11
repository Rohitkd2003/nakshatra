from django.urls import path
from .views import (
    PatientMeView,
    TemplateListView,
    PatientConfigView,
    VitalsView,
    PatientDetailsView,
)

urlpatterns = [
    path("me", PatientMeView.as_view()),
    path("templates", TemplateListView.as_view()),
    path("me/config", PatientConfigView.as_view()),
    path("me/vitals", VitalsView.as_view()),
    path("me/details", PatientDetailsView.as_view()),
]
