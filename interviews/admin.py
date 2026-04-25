from django.contrib import admin
from .models import Interview

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ['application', 'date', 'time', 'mode', 'created_at']
    list_filter = ['mode', 'date', 'created_at']
    search_fields = ['application__candidate__full_name', 'application__job__title']
    date_hierarchy = 'date'
