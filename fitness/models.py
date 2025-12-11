from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class FitnessPlan(models.Model):
    PLAN_TYPE_CHOICES = (
        ('Yoga', 'Yoga'),
        ('Workout', 'Workout'),
        ('General', 'General'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    plan_type = models.CharField(max_length=50, choices=PLAN_TYPE_CHOICES, default='General')
    duration_minutes = models.IntegerField(default=30)
    intensity = models.CharField(max_length=50, default='Medium')
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.plan_type})"


class FitnessExercise(models.Model):
    plan = models.ForeignKey(FitnessPlan, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_seconds = models.IntegerField(default=60)
    repetitions = models.IntegerField(default=1)
    order = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} ({self.plan.name})"


class WorkoutLog(models.Model):
    patient = models.ForeignKey(User, related_name='workout_logs', on_delete=models.CASCADE)
    plan = models.ForeignKey(FitnessPlan, related_name='logs', on_delete=models.SET_NULL, null=True)
    plan_name = models.CharField(max_length=200)  # snapshot
    date = models.DateField()
    time = models.TimeField()
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    logged_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.calories_burned and self.plan:
            # simple formula: duration * intensity_factor
            intensity_map = {'Low': 4, 'Medium': 6, 'High': 8}
            factor = intensity_map.get(self.plan.intensity, 6)
            self.calories_burned = int(self.duration_minutes * factor)
        super().save(*args, **kwargs)

from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories_burned = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
