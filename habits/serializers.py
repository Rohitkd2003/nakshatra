from rest_framework import serializers
from .models import HabitTemplate, Habit, HabitLog

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
