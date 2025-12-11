from django.urls import path
from .views import HealthMetricCreateView, HealthMetricListView

urlpatterns = [
    path("log/", HealthMetricCreateView.as_view(), name="metric-create"),
    path("list/", HealthMetricListView.as_view(), name="metric-list"),
]
