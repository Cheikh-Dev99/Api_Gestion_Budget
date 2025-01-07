# budgetsApp/views/reinitialiser.py
from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email from Django.'
    from_email = 'cheikhahmedtidiane220@gmail.com'
    recipient_list = ['cheikhahmedtidiane219@gmail.com']

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending email: {e}")
