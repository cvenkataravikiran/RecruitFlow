from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    """Form for creating and editing jobs"""
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'salary_min', 'salary_max', 
                  'description', 'skills_required', 'job_type', 'deadline', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Senior Python Developer'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Mumbai, India or New York, USA'}),
            'salary_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 500000 (INR) or 50000 (USD)'}),
            'salary_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 1200000 (INR) or 120000 (USD)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'skills_required': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'e.g., Python, Django, PostgreSQL'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
