# metrics/models.py
from django.db import models
from django.conf import settings

class HealthMetric(models.Model):
    METRIC_TYPE_CHOICES = (
        ('Weight', 'Weight'),
        ('BMI', 'BMI'),
        ('Blood Pressure', 'Blood Pressure'),
        ('Heart Rate', 'Heart Rate'),
        ('Blood Sugar', 'Blood Sugar'),
        ('Other', 'Other'),
    )

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='metrics'
    )
    metric_type = models.CharField(max_length=50, choices=METRIC_TYPE_CHOICES)
    value = models.FloatField()
    unit = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_type} - {self.value} ({self.patient})"
