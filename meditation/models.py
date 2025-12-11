from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class MeditationPlan(models.Model):
    PLAN_TYPE_CHOICES = (
        ('Mindfulness', 'Mindfulness'),
        ('Breathing', 'Breathing'),
        ('Relaxation', 'Relaxation'),
        ('General', 'General'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    plan_type = models.CharField(max_length=50, choices=PLAN_TYPE_CHOICES, default='General')
    duration_minutes = models.IntegerField(default=10)
    audio_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.plan_type})"


class MeditationSession(models.Model):
    patient = models.ForeignKey(User, related_name='meditation_sessions', on_delete=models.CASCADE)
    plan = models.ForeignKey(MeditationPlan, related_name='sessions', on_delete=models.SET_NULL, null=True)
    plan_name = models.CharField(max_length=200)  # snapshot
    date = models.DateField()
    time = models.TimeField()
    duration_minutes = models.IntegerField()
    mood_before = models.CharField(max_length=50, blank=True, null=True)
    mood_after = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    logged_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.duration_minutes and self.plan:
            self.duration_minutes = self.plan.duration_minutes
        if not self.plan_name and self.plan:
            self.plan_name = self.plan.name
        super().save(*args, **kwargs)
