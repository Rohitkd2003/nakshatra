from django.db import models

# Create your models here.
from django.db import models
from auth_app.models import User

class PatientConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="config")
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    target_calories = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} Config"


class HealthTemplate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class VitalRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vitals")
    vital_type = models.CharField(max_length=50)   # e.g. heart_rate, bp
    value = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.vital_type}"
