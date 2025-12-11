from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MeditationPlan, MeditationSession

@admin.register(MeditationPlan)
class MeditationPlanAdmin(admin.ModelAdmin):
    list_display = ('id','name','plan_type','duration_minutes','created_at')

@admin.register(MeditationSession)
class MeditationSessionAdmin(admin.ModelAdmin):
    list_display = ('id','patient','plan_name','date','time','duration_minutes','logged_at')
