from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    """Form for job application"""
    class Meta:
        model = Application
        fields = ['cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write a brief cover letter (optional)...'
            }),
        }

class ApplicationStatusForm(forms.ModelForm):
    """Form for updating application status"""
    class Meta:
        model = Application
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
