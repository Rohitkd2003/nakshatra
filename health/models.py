from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class VitalType(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class VitalLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vital_type = models.ForeignKey(VitalType, on_delete=models.CASCADE)
    value = models.FloatField()
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.vital_type.name}"
