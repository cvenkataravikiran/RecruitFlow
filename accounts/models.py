from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class CandidateProfile(models.Model):
    """Profile for job candidates"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    
    # Professional Summary
    professional_summary = models.TextField(blank=True, help_text="Brief professional summary")
    
    # Skills - Structured
    skills = models.TextField(blank=True, help_text="Comma-separated skills")
    
    # Experience - Structured Fields
    experience = models.TextField(blank=True)  # Keep for backward compatibility
    current_company = models.CharField(max_length=200, blank=True)
    current_position = models.CharField(max_length=200, blank=True)
    years_of_experience = models.CharField(max_length=50, blank=True, help_text="e.g., 3 years")
    
    # Education - Structured Fields
    education = models.TextField(blank=True)  # Keep for backward compatibility
    highest_degree = models.CharField(max_length=200, blank=True, help_text="e.g., Bachelor's, Master's, PhD")
    field_of_study = models.CharField(max_length=200, blank=True, help_text="e.g., Computer Science")
    university = models.CharField(max_length=200, blank=True)
    graduation_year = models.CharField(max_length=10, blank=True, help_text="e.g., 2020")
    
    # Additional Information
    location = models.CharField(max_length=200, blank=True, help_text="City, Country")
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn profile URL")
    github_url = models.URLField(blank=True, help_text="GitHub profile URL")
    portfolio_url = models.URLField(blank=True, help_text="Portfolio website URL")
    
    # Files
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - Candidate"

    def profile_completeness(self):
        """Calculate profile completion percentage"""
        fields = [
            self.full_name, self.phone, self.professional_summary, self.skills, 
            self.current_company, self.current_position, self.years_of_experience,
            self.highest_degree, self.field_of_study, self.university, 
            self.graduation_year, self.location, self.resume
        ]
        filled = sum(1 for field in fields if field)
        return int((filled / len(fields)) * 100)


class RecruiterProfile(models.Model):
    """Profile for recruiters/HR"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruiter_profile')
    company_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100, blank=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    
    # Additional Company Information
    company_website = models.URLField(blank=True, help_text="Company website URL")
    company_size = models.CharField(max_length=50, blank=True, help_text="e.g., 50-100 employees")
    industry = models.CharField(max_length=100, blank=True, help_text="e.g., Technology, Finance")
    location = models.CharField(max_length=200, blank=True, help_text="Company location")
    about_company = models.TextField(blank=True, help_text="Brief description about the company")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.user.username}"


class Notification(models.Model):
    """Notifications for users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification for {self.user.username}"
