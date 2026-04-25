from django.urls import path
from . import views

app_name = 'interviews'

urlpatterns = [
    path('schedule/<int:application_id>/', views.schedule_interview, name='schedule_interview'),
    path('my-interviews/', views.my_interviews, name='my_interviews'),
    path('recruiter-interviews/', views.recruiter_interviews, name='recruiter_interviews'),
]
