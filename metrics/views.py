from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import HealthMetric
from .serializers import HealthMetricSerializer, HealthMetricCreateSerializer

# ----------------------------
# 1) CREATE HEALTH METRIC
# ----------------------------
class HealthMetricCreateView(generics.CreateAPIView):
    queryset = HealthMetric.objects.all()
    serializer_class = HealthMetricCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)


# ----------------------------
# 2) LIST HEALTH METRICS
# ----------------------------
class HealthMetricListView(generics.ListAPIView):
    serializer_class = HealthMetricSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("start_date", openapi.IN_QUERY, type=openapi.TYPE_STRING, format="date", required=False),
            openapi.Parameter("end_date", openapi.IN_QUERY, type=openapi.TYPE_STRING, format="date", required=False),
        ]
    )
    def get_queryset(self):
        user = self.request.user
        qs = HealthMetric.objects.filter(patient=user).order_by('-logged_at')

        # Optional filters
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")

        if start_date and end_date:
            qs = qs.filter(date__range=[start_date, end_date])

        return qs
