from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('job/<int:job_id>/applicants/', views.job_applicants, name='job_applicants'),
    path('<int:application_id>/update-status/', views.update_application_status, name='update_status'),
    path('<int:application_id>/candidate/', views.candidate_detail, name='candidate_detail'),
]
