from rest_framework import serializers
from .models import MeditationPlan, MeditationSession

class MeditationPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationPlan
        fields = ['id','name','plan_type','description','duration_minutes','audio_url','created_at']

class MeditationSessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationSession
        fields = ['plan','date','time','duration_minutes','mood_before','mood_after','notes']

    def create(self, validated_data):
        request = self.context['request']
        plan = validated_data.get('plan')
        session = MeditationSession.objects.create(
            patient = request.user,
            plan = plan,
            plan_name = plan.name if plan else 'Unknown',
            date = validated_data['date'],
            time = validated_data['time'],
            duration_minutes = validated_data.get('duration_minutes') or (plan.duration_minutes if plan else 10),
            mood_before = validated_data.get('mood_before',''),
            mood_after = validated_data.get('mood_after',''),
            notes = validated_data.get('notes','')
        )
        return session

class MeditationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationSession
        fields = ['id','patient','plan','plan_name','date','time','duration_minutes','mood_before','mood_after','notes','logged_at']
        read_only_fields = ['id','patient','plan_name','logged_at']
