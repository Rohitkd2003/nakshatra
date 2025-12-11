from django.urls import path
from .views import VitalTypeListView, VitalLogListCreateView

urlpatterns = [
    path("vital-types/", VitalTypeListView.as_view()),
    path("vital-logs/", VitalLogListCreateView.as_view()),
]
