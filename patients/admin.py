from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import PatientConfig, VitalRecord
from habits.models import Habit
from consultations.models import Consultation
from fitness.models import WorkoutLog
from meditation.models import MeditationSession
from metrics.models import HealthMetric
from nutrition.models import MealLog, CalorieEntry

User = get_user_model()

class Patient(User):
    class Meta:
        proxy = True
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

# Inline for PatientConfig
class PatientConfigInline(admin.StackedInline):
    model = PatientConfig
    extra = 0  # extra = 0, karan ekach config honar
    max_num = 1

# Inline for VitalRecord
class VitalInline(admin.TabularInline):
    model = VitalRecord
    extra = 1


class HabitInline(admin.TabularInline):
    model = Habit
    extra = 0


class ConsultationInline(admin.TabularInline):
    model = Consultation
    fk_name = "patient"
    extra = 0


class WorkoutLogInline(admin.TabularInline):
    model = WorkoutLog
    extra = 0


class MeditationSessionInline(admin.TabularInline):
    model = MeditationSession
    extra = 0


class HealthMetricInline(admin.TabularInline):
    model = HealthMetric
    extra = 0


class MealLogInline(admin.TabularInline):
    model = MealLog
    extra = 0


class CalorieEntryInline(admin.TabularInline):
    model = CalorieEntry
    extra = 0

# Admin for Patients
@admin.register(Patient)
class PatientAdmin(BaseUserAdmin):
    """Custom Patient Admin for separate 'Patients' panel"""

    fieldsets = (
        (None, {"fields": ("email", "password")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )

    exclude = (
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
        "user_permissions",
        "last_login",
        "date_joined",
        "first_name",
        "last_name",
        "username",
        "role",
        "phone",
    )

    list_display = ("id", "email")
    search_fields = ("email",)
    ordering = ["email"]

    inlines = [
        PatientConfigInline,
        VitalInline,
        HabitInline,
        ConsultationInline,
        WorkoutLogInline,
        MeditationSessionInline,
        HealthMetricInline,
        MealLogInline,
        CalorieEntryInline,
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_staff=False)

    def save_related(self, request, form, formsets, change):
        """
        Prevent duplicate PatientConfig creation by letting inline handle creation.
        """
        super().save_related(request, form, formsets, change)

    def save_model(self, request, obj, form, change):
        obj.is_staff = False
        obj.is_superuser = False
        super().save_model(request, obj, form, change)  # config auto-create will be handled by inline

    def get_model_perms(self, request):
        return {
            "add": True,
            "change": True,
            "delete": True,
        }

