"""
URL configuration for recruitflow project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from accounts import views as account_views

def contact_view(request):
    """Handle contact form submissions via Web3Forms"""
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        if name and email and subject and message:
            try:
                import requests
                
                # Send via Web3Forms API
                response = requests.post(
                    'https://api.web3forms.com/submit',
                    data={
                        'access_key': settings.WEB3FORMS_ACCESS_KEY,
                        'name': name,
                        'email': email,
                        'subject': subject,
                        'message': message
                    }
                )
                
                if response.status_code == 200:
                    messages.success(request, 'Your message has been sent successfully!')
                else:
                    messages.error(request, 'Failed to send message. Please try again later.')
            except Exception as e:
                messages.error(request, 'Failed to send message. Please try again later.')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'contact.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.home, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', contact_view, name='contact'),
    path('accounts/', include('accounts.urls')),
    path('jobs/', include('jobs.urls')),
    path('applications/', include('applications.urls')),
    path('interviews/', include('interviews.urls')),
    path('dashboard/', include('dashboard.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
