from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FitnessPlan, FitnessExercise, WorkoutLog

class ExerciseInline(admin.TabularInline):
    model = FitnessExercise
    extra = 1

@admin.register(FitnessPlan)
class FitnessPlanAdmin(admin.ModelAdmin):
    list_display = ('id','name','plan_type','duration_minutes','intensity','created_at')
    inlines = [ExerciseInline]

@admin.register(WorkoutLog)
class WorkoutLogAdmin(admin.ModelAdmin):
    list_display = ('id','patient','plan_name','date','time','duration_minutes','calories_burned','logged_at')
