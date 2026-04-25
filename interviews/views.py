from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Interview
from .forms import InterviewForm
from applications.models import Application
from accounts.decorators import candidate_required, recruiter_required
from accounts.models import Notification
from accounts.email_utils import send_notification_email

@login_required
@recruiter_required
def schedule_interview(request, application_id):
    """Schedule an interview for an application"""
    application = get_object_or_404(Application, pk=application_id, job__recruiter=request.user.recruiter_profile)
    
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.application = application
            interview.save()
            
            # Update application status
            application.status = 'interview_scheduled'
            application.save()
            
            # Create notification for candidate
            Notification.objects.create(
                user=application.candidate.user,
                message=f"Interview scheduled for {application.job.title} on {interview.date} at {interview.time}"
            )
            
            # Send email notification to candidate (optional)
            interview_details = f"Date: {interview.date}\nTime: {interview.time}\nMode: {interview.get_mode_display()}"
            if interview.meeting_link:
                interview_details += f"\nMeeting Link: {interview.meeting_link}"
            
            send_notification_email(
                subject=f"Interview Scheduled - {application.job.title}",
                message=f"Hello {application.candidate.full_name},\n\nYour interview has been scheduled for {application.job.title}.\n\n{interview_details}\n\nPlease be prepared and join on time.\n\nBest regards,\nRecruitFlow Team",
                recipient_email=application.candidate.user.email
            )
            
            messages.success(request, 'Interview scheduled successfully!')
            return redirect('applications:job_applicants', job_id=application.job.id)
    else:
        form = InterviewForm()
    
    context = {
        'form': form,
        'application': application,
    }
    return render(request, 'interviews/schedule_interview.html', context)

@login_required
@candidate_required
def my_interviews(request):
    """View candidate's scheduled interviews"""
    applications = Application.objects.filter(candidate=request.user.candidate_profile)
    interviews = Interview.objects.filter(application__in=applications)
    
    context = {
        'interviews': interviews,
    }
    return render(request, 'interviews/my_interviews.html', context)

@login_required
@recruiter_required
def recruiter_interviews(request):
    """View recruiter's scheduled interviews"""
    jobs = request.user.recruiter_profile.jobs.all()
    applications = Application.objects.filter(job__in=jobs)
    interviews = Interview.objects.filter(application__in=applications)
    
    context = {
        'interviews': interviews,
    }
    return render(request, 'interviews/recruiter_interviews.html', context)
