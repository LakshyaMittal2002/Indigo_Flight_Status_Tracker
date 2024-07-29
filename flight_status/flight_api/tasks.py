
from celery import shared_task
from django.core.mail import send_mail
from .models import Notification

@shared_task
def send_notification_task(customer_email, message, flight_id, customer_id):
    print(f"Task started: send_notification_task for customer_email: {customer_email}")
    try:
        send_mail(
            subject='Flight Update Notification',
            message=message,
            from_email='lmittal2002@gmail.com',
            recipient_list=[customer_email],
            fail_silently=False,
        )
        print(f"Email sent to {customer_email}")

        # Create a notification record
        Notification.objects.create(
            customer_id=customer_id,
            flight_id=flight_id,
            message=message,
            channel='email'
        )
        print(f"Notification created for customer {customer_id}")
    except Exception as e:
        print(f"Error in send_notification_task: {e}")
