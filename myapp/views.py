from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings

def send_test_email(request):
    subject = 'Test Email from Django'
    message = 'This is a test email sent from Django using SMTP on Liara server.'
    recipient_list = ['some@example.com']
    # cc_email  = ['test.one@example.com', 'test.two@example.com']
    # bcc_email = ['test.one@example.com', 'test.two@example.com']
    
    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_FROM_ADDRESS,
        recipient_list,
        # cc=cc_email,
        # bcc=bcc_email,
        headers={"x-liara-tag": "test-tag"},
    )

    email.send(fail_silently=False)
    return HttpResponse('Test email sent successfully!')
