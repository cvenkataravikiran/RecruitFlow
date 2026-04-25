from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from accounts.decorators import candidate_required, recruiter_required
from applications.models import Application
from jobs.models import Job
from interviews.models import Interview

@login_required
@candidate_required
def candidate_dashboard(request):
    """Candidate dashboard view"""
    candidate = request.user.candidate_profile
    
    # Get statistics
    total_applications = Application.objects.filter(candidate=candidate).count()
    shortlisted = Application.objects.filter(candidate=candidate, status='shortlisted').count()
    interviews = Interview.objects.filter(application__candidate=candidate).count()
    
    # Recent applications
    recent_applications = Application.objects.filter(candidate=candidate)[:5]
    
    # Upcoming interviews
    upcoming_interviews = Interview.objects.filter(application__candidate=candidate).order_by('date', 'time')[:5]
    
    # Profile completeness
    profile_completeness = candidate.profile_completeness()
    
    context = {
        'total_applications': total_applications,
        'shortlisted': shortlisted,
        'interviews': interviews,
        'recent_applications': recent_applications,
        'upcoming_interviews': upcoming_interviews,
        'profile_completeness': profile_completeness,
    }
    return render(request, 'dashboard/candidate_dashboard.html', context)

@login_required
@recruiter_required
def recruiter_dashboard(request):
    """Recruiter dashboard view"""
    recruiter = request.user.recruiter_profile
    
    # Get statistics
    total_jobs = Job.objects.filter(recruiter=recruiter).count()
    active_jobs = Job.objects.filter(recruiter=recruiter, is_active=True).count()
    total_applications = Application.objects.filter(job__recruiter=recruiter).count()
    
    # Applications by status
    status_counts = Application.objects.filter(job__recruiter=recruiter).values('status').annotate(count=Count('status'))
    
    # Recent jobs
    recent_jobs = Job.objects.filter(recruiter=recruiter).order_by('-created_at')[:5]
    
    # Recent applications
    recent_applications = Application.objects.filter(job__recruiter=recruiter).order_by('-applied_at')[:10]
    
    # Upcoming interviews
    upcoming_interviews = Interview.objects.filter(application__job__recruiter=recruiter).order_by('date', 'time')[:5]
    
    context = {
        'total_jobs': total_jobs,
        'active_jobs': active_jobs,
        'total_applications': total_applications,
        'status_counts': status_counts,
        'recent_jobs': recent_jobs,
        'recent_applications': recent_applications,
        'upcoming_interviews': upcoming_interviews,
    }
    return render(request, 'dashboard/recruiter_dashboard.html', context)
