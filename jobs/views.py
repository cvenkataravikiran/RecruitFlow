from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Job
from .forms import JobForm
from accounts.decorators import recruiter_required

def job_list(request):
    """Public job listing page"""
    jobs = Job.objects.filter(is_active=True)
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(company__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(skills_required__icontains=search_query)
        )
    
    # Filter by job type
    job_type = request.GET.get('job_type', '')
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    
    # Pagination
    paginator = Paginator(jobs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'job_type': job_type,
    }
    return render(request, 'jobs/job_list.html', context)

def job_detail(request, pk):
    """Job detail page"""
    job = get_object_or_404(Job, pk=pk, is_active=True)
    
    # Check if user has already applied
    has_applied = False
    if request.user.is_authenticated and hasattr(request.user, 'candidate_profile'):
        from applications.models import Application
        has_applied = Application.objects.filter(
            candidate=request.user.candidate_profile,
            job=job
        ).exists()
    
    context = {
        'job': job,
        'has_applied': has_applied,
    }
    return render(request, 'jobs/job_detail.html', context)

@login_required
@recruiter_required
def job_create(request):
    """Create new job posting"""
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user.recruiter_profile
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('dashboard:recruiter_dashboard')
    else:
        form = JobForm()
    
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Post New Job'})

@login_required
@recruiter_required
def job_edit(request, pk):
    """Edit job posting"""
    job = get_object_or_404(Job, pk=pk, recruiter=request.user.recruiter_profile)
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('dashboard:recruiter_dashboard')
    else:
        form = JobForm(instance=job)
    
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Edit Job', 'job': job})

@login_required
@recruiter_required
def job_delete(request, pk):
    """Delete job posting"""
    job = get_object_or_404(Job, pk=pk, recruiter=request.user.recruiter_profile)
    
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('dashboard:recruiter_dashboard')
    
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})
