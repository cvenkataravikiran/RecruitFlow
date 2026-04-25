"""
Email utility functions for sending notifications
"""
from django.core.mail import send_mail
from django.conf import settings


def send_notification_email(subject, message, recipient_email):
    """
    Send email notification to user
    Optional: Only sends if EMAIL_HOST_USER is configured
    
    Args:
        subject: Email subject
        message: Email body
        recipient_email: Recipient's email address
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    # Check if email is configured
    if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
        # Email not configured, skip silently
        return False
    
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=True,  # Don't raise errors if email fails
        )
        return True
    except Exception as e:
        # Log error but don't break the application
        print(f"Email sending failed: {e}")
        return False
