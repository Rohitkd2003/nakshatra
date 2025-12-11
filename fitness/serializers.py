from rest_framework import serializers
from .models import FitnessPlan, FitnessExercise, WorkoutLog

class FitnessExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessExercise
        fields = ['name','description','duration_seconds','repetitions','order']

class FitnessPlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessPlan
        fields = ['id','name','plan_type','description','duration_minutes','intensity','video_url','created_at']

class FitnessPlanDetailSerializer(serializers.ModelSerializer):
    exercises = FitnessExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = FitnessPlan
        fields = ['id','name','plan_type','description','duration_minutes','intensity','video_url','exercises']

class WorkoutLogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutLog
        fields = ['plan','date','time','duration_minutes','notes']

    def create(self, validated_data):
        request = self.context['request']
        plan = validated_data.get('plan')
        plan_name = plan.name if plan else 'Unknown'
        duration = validated_data.get('duration_minutes') or (plan.duration_minutes if plan else 30)
        wl = WorkoutLog.objects.create(
            patient = request.user,
            plan = plan,
            plan_name = plan_name,
            date = validated_data['date'],
            time = validated_data['time'],
            duration_minutes = duration,
            notes = validated_data.get('notes','')
        )
        return wl

class WorkoutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutLog
        fields = ['id','patient','plan','plan_name','date','time','duration_minutes','calories_burned','notes','logged_at']
        read_only_fields = ['id','patient','plan_name','calories_burned','logged_at']

from rest_framework import serializers
from .models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
