from django.db import models
from auth_app.models import User

class Consultation(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    )

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="patient_consultations"
    )

    doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="doctor_consultations"
    )

    reason = models.TextField()
    date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient.email} — {self.status}"
