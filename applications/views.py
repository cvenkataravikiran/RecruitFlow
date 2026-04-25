from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Application
from .forms import ApplicationForm, ApplicationStatusForm
from jobs.models import Job
from accounts.decorators import candidate_required, recruiter_required
from accounts.models import Notification
from accounts.email_utils import send_notification_email

@login_required
@candidate_required
def apply_job(request, job_id):
    """Apply for a job"""
    job = get_object_or_404(Job, pk=job_id, is_active=True)
    candidate = request.user.candidate_profile
    
    # Check if already applied
    if Application.objects.filter(candidate=candidate, job=job).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('jobs:job_detail', pk=job_id)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.candidate = candidate
            application.job = job
            application.save()
            
            # Create notification for recruiter
            Notification.objects.create(
                user=job.recruiter.user,
                message=f"New application from {candidate.full_name} for {job.title}"
            )
            
            # Send email notification to recruiter (optional)
            send_notification_email(
                subject=f"New Application for {job.title}",
                message=f"Hello,\n\nYou have received a new application from {candidate.full_name} for the position of {job.title}.\n\nPlease login to your dashboard to review the application.\n\nBest regards,\nRecruitFlow Team",
                recipient_email=job.recruiter.user.email
            )
            
            messages.success(request, 'Application submitted successfully!')
            return redirect('applications:my_applications')
    else:
        form = ApplicationForm()
    
    return render(request, 'applications/apply.html', {'form': form, 'job': job})

@login_required
@candidate_required
def my_applications(request):
    """View candidate's applications"""
    applications = Application.objects.filter(candidate=request.user.candidate_profile)
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    # Pagination
    paginator = Paginator(applications, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'status_filter': status_filter,
    }
    return render(request, 'applications/my_applications.html', context)

@login_required
@recruiter_required
def job_applicants(request, job_id):
    """View applicants for a job"""
    job = get_object_or_404(Job, pk=job_id, recruiter=request.user.recruiter_profile)
    applications = Application.objects.filter(job=job)
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    # Pagination
    paginator = Paginator(applications, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'job': job,
        'page_obj': page_obj,
        'status_filter': status_filter,
    }
    return render(request, 'applications/job_applicants.html', context)

@login_required
@recruiter_required
def update_application_status(request, application_id):
    """Update application status"""
    application = get_object_or_404(Application, pk=application_id, job__recruiter=request.user.recruiter_profile)
    
    if request.method == 'POST':
        form = ApplicationStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            
            # Create notification for candidate
            Notification.objects.create(
                user=application.candidate.user,
                message=f"Your application for {application.job.title} has been updated to {application.get_status_display()}"
            )
            
            # Send email notification to candidate (optional)
            send_notification_email(
                subject=f"Application Status Update - {application.job.title}",
                message=f"Hello {application.candidate.full_name},\n\nYour application for {application.job.title} has been updated.\n\nNew Status: {application.get_status_display()}\n\nPlease login to your dashboard for more details.\n\nBest regards,\nRecruitFlow Team",
                recipient_email=application.candidate.user.email
            )
            
            messages.success(request, 'Application status updated successfully!')
            return redirect('applications:job_applicants', job_id=application.job.id)
    else:
        form = ApplicationStatusForm(instance=application)
    
    return render(request, 'applications/update_status.html', {'form': form, 'application': application})

@login_required
@recruiter_required
def candidate_detail(request, application_id):
    """View candidate details"""
    application = get_object_or_404(Application, pk=application_id, job__recruiter=request.user.recruiter_profile)
    
    context = {
        'application': application,
        'candidate': application.candidate,
    }
    return render(request, 'applications/candidate_detail.html', context)
