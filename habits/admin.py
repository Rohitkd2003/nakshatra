from django.contrib import admin
from .models import HabitTemplate, Habit, HabitLog

admin.site.register(HabitTemplate)
admin.site.register(Habit)
admin.site.register(HabitLog)
