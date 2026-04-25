from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('candidate/', views.candidate_dashboard, name='candidate_dashboard'),
    path('recruiter/', views.recruiter_dashboard, name='recruiter_dashboard'),
]
