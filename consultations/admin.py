from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Consultation

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "date", "status")
    list_filter = ("status", "date")
    search_fields = ("patient__email", "doctor__email", "reason")
