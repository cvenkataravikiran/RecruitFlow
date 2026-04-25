from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def candidate_required(view_func):
    """Decorator to check if user is a candidate"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Please login to access this page.')
            return redirect('accounts:login')
        if hasattr(request.user, 'candidate_profile'):
            return view_func(request, *args, **kwargs)
        messages.error(request, 'You need to be a candidate to access this page.')
        if hasattr(request.user, 'recruiter_profile'):
            return redirect('dashboard:recruiter_dashboard')
        return redirect('home')
    return wrapper

def recruiter_required(view_func):
    """Decorator to check if user is a recruiter"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Please login to access this page.')
            return redirect('accounts:login')
        if hasattr(request.user, 'recruiter_profile'):
            return view_func(request, *args, **kwargs)
        messages.error(request, 'You need to be a recruiter to access this page.')
        if hasattr(request.user, 'candidate_profile'):
            return redirect('dashboard:candidate_dashboard')
        return redirect('home')
    return wrapper
