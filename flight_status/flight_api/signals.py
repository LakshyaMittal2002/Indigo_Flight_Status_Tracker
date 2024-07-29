# signals.py
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Flight, Booking
from .tasks import send_notification_task

@receiver(post_save, sender=Flight)
def send_flight_update_notification(sender, instance, **kwargs):
    bookings = Booking.objects.filter(flight=instance)
    for booking in bookings:
        customer = booking.customer
        message = f"Flight {instance.flight_number} status has been updated to {instance.status}."
        send_notification_task.delay(customer.email, message, instance.id, customer.id)


