from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Meal, MealIngredient, MealLog, CalorieEntry

class IngredientInline(admin.TabularInline):
    model = MealIngredient
    extra = 1

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('id','name','condition','calories','created_at')
    inlines = [IngredientInline]

@admin.register(MealLog)
class MealLogAdmin(admin.ModelAdmin):
    list_display = ('id','patient','meal_name','date','time','calories','logged_at')

@admin.register(CalorieEntry)
class CalorieEntryAdmin(admin.ModelAdmin):
    list_display = ('id','patient','food_description','calories','date','time','created_at')
