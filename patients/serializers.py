from rest_framework import serializers
from .models import PatientConfig, HealthTemplate, VitalRecord
from community.models import Post, Comment
from consultations.models import Consultation
from fitness.models import FitnessPlan, WorkoutLog
from habits.models import HabitTemplate, Habit, HabitLog
from health.models import VitalType, VitalLog
from meditation.models import MeditationPlan, MeditationSession
from metrics.models import HealthMetric
from nutrition.models import Meal, MealLog, CalorieEntry

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTemplate
        fields = "__all__"


class PatientConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientConfig
        fields = "__all__"
        read_only_fields = ["user"]


class VitalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalRecord
        fields = "__all__"
        read_only_fields = ["user", "timestamp"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = "__all__"


class FitnessPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessPlan
        fields = "__all__"


class WorkoutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutLog
        fields = "__all__"


class HabitTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitTemplate
        fields = "__all__"


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"


class HabitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitLog
        fields = "__all__"


class VitalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalType
        fields = "__all__"


class VitalLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalLog
        fields = "__all__"


class MeditationPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationPlan
        fields = "__all__"


class MeditationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationSession
        fields = "__all__"


class HealthMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetric
        fields = "__all__"


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"


class MealLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealLog
        fields = "__all__"


class CalorieEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieEntry
        fields = "__all__"
