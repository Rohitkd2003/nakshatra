from django.contrib import admin
from .models import HealthMetric

@admin.register(HealthMetric)
class HealthMetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'metric_type', 'value', 'unit', 'date', 'time', 'logged_at')
    list_filter = ('metric_type', 'date')
    search_fields = ('patient__username', 'metric_type')
