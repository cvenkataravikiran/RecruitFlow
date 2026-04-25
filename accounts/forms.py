from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CandidateProfile, RecruiterProfile

class UserRegistrationForm(UserCreationForm):
    """User registration form with role selection"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    role = forms.ChoiceField(choices=[('candidate', 'Candidate'), ('recruiter', 'Recruiter')], required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CandidateProfileForm(forms.ModelForm):
    """Form for candidate profile"""
    class Meta:
        model = CandidateProfile
        fields = [
            'full_name', 'phone', 'location', 'professional_summary',
            'skills', 'current_company', 'current_position', 'years_of_experience',
            'highest_degree', 'field_of_study', 'university', 'graduation_year',
            'linkedin_url', 'github_url', 'portfolio_url',
            'resume', 'profile_image'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91 9876543210 or +1 234 567 8900'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mumbai, India or New York, USA'}),
            'professional_summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief summary of your professional background and career goals...'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Python, Django, JavaScript, React, SQL, Git'}),
            'current_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ABC Tech Solutions'}),
            'current_position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Senior Software Engineer'}),
            'years_of_experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '5 years'}),
            'highest_degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Bachelor's in Computer Science"}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Computer Science'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IIT Bombay, MIT, Stanford'}),
            'graduation_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2020'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/yourprofile'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/yourusername'}),
            'portfolio_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://yourportfolio.com'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class RecruiterProfileForm(forms.ModelForm):
    """Form for recruiter profile"""
    class Meta:
        model = RecruiterProfile
        fields = ['company_name', 'designation', 'phone', 'company_website', 'company_size', 'industry', 'location', 'about_company', 'company_logo']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ABC Tech Solutions'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HR Manager'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 234 567 8900'}),
            'company_website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.company.com'}),
            'company_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '50-100 employees'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Technology'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'San Francisco, USA'}),
            'about_company': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Brief description about your company...'}),
            'company_logo': forms.FileInput(attrs={'class': 'form-control'}),
        }
