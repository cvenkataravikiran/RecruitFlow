from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegistrationForm, CandidateProfileForm, RecruiterProfileForm
from .models import CandidateProfile, RecruiterProfile
from jobs.models import Job

def home(request):
    """Home page with featured jobs - redirects logged-in users to their dashboard"""
    # Redirect authenticated users to their respective dashboards
    if request.user.is_authenticated:
        if hasattr(request.user, 'candidate_profile'):
            return redirect('dashboard:candidate_dashboard')
        elif hasattr(request.user, 'recruiter_profile'):
            return redirect('dashboard:recruiter_dashboard')
    
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')[:6]
    context = {
        'jobs': jobs,
        'total_jobs': Job.objects.filter(is_active=True).count()
    }
    return render(request, 'home.html', context)

def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            
            # Create profile based on role
            if role == 'candidate':
                CandidateProfile.objects.create(
                    user=user,
                    full_name=f"{user.first_name} {user.last_name}"
                )
            elif role == 'recruiter':
                RecruiterProfile.objects.create(
                    user=user,
                    company_name="Company Name"
                )
            
            messages.success(request, 'Registration successful! Please login.')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                
                # Redirect based on role
                if hasattr(user, 'candidate_profile'):
                    return redirect('dashboard:candidate_dashboard')
                elif hasattr(user, 'recruiter_profile'):
                    return redirect('dashboard:recruiter_dashboard')
                else:
                    return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile(request):
    """User profile view"""
    if hasattr(request.user, 'candidate_profile'):
        profile = request.user.candidate_profile
        if request.method == 'POST':
            form = CandidateProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('accounts:profile')
        else:
            form = CandidateProfileForm(instance=profile)
        return render(request, 'accounts/candidate_profile.html', {'form': form, 'profile': profile})
    
    elif hasattr(request.user, 'recruiter_profile'):
        profile = request.user.recruiter_profile
        if request.method == 'POST':
            form = RecruiterProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('accounts:profile')
        else:
            form = RecruiterProfileForm(instance=profile)
        return render(request, 'accounts/recruiter_profile.html', {'form': form, 'profile': profile})
    
    else:
        messages.error(request, 'Profile not found.')
        return redirect('home')
