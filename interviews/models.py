from django.db import models
from applications.models import Application

class Interview(models.Model):
    """Interview scheduling model"""
    MODE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='interviews')
    date = models.DateField()
    time = models.TimeField()
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='online')
    meeting_link = models.URLField(blank=True, help_text="For online interviews")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"Interview for {self.application.candidate.full_name} - {self.application.job.title}"
