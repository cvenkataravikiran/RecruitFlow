from django import forms
from .models import Interview

class InterviewForm(forms.ModelForm):
    """Form for scheduling interviews"""
    class Meta:
        model = Interview
        fields = ['date', 'time', 'mode', 'meeting_link', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'mode': forms.Select(attrs={'class': 'form-control'}),
            'meeting_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://meet.google.com/...'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Additional notes for the interview...'}),
        }
