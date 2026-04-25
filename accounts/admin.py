from django.contrib import admin
from .models import CandidateProfile, RecruiterProfile, Notification

@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'phone', 'created_at']
    search_fields = ['full_name', 'user__username', 'skills']
    list_filter = ['created_at']

@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'user', 'designation', 'phone', 'created_at']
    search_fields = ['company_name', 'user__username']
    list_filter = ['created_at']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['user__username', 'message']
