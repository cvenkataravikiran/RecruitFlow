from django.db import models
from accounts.models import CandidateProfile
from jobs.models import Job

class Application(models.Model):
    """Job application model"""
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]

    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    cover_letter = models.TextField(blank=True)

    class Meta:
        ordering = ['-applied_at']
        unique_together = ['candidate', 'job']

    def __str__(self):
        return f"{self.candidate.full_name} - {self.job.title}"

    def get_status_badge_class(self):
        """Return Bootstrap badge class based on status"""
        status_classes = {
            'applied': 'bg-primary',
            'shortlisted': 'bg-warning',
            'interview_scheduled': 'bg-info',
            'selected': 'bg-success',
            'rejected': 'bg-danger',
        }
        return status_classes.get(self.status, 'bg-secondary')
