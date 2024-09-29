from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def send_test_email(request):
    subject = 'Test Email from Django'
    message = 'This is a test email sent from Django using SMTP on Liara server.'
    recipient_list = ['recipient@example.com']
    
    send_mail(
        subject,
        message,
        settings.EMAIL_FROM_ADDRESS,
        recipient_list,
        fail_silently=False,
    )
    
    return HttpResponse('Test email sent successfully!')
