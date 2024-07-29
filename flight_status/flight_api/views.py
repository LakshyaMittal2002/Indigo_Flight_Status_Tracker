from django.shortcuts import render

from rest_framework import viewsets
from .models import Customer, Flight, Notification,Booking
from .serializers import CustomerSerializer, FlightSerializer, NotificationSerializer,BookingSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    send_mail(
        'Test Email',
        'This is a test email.',
        'lmittal2002@gmail.com',
        ['goencode2002@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Test email sent.")

from .tasks import send_notification_task

def test_task(request):
    customer_email = 'goencode2002@gmail.com'  # Use a test email
    message = 'This is a test notification.'
    flight_id = 1
    customer_id = 7
    send_notification_task.delay(customer_email, message, flight_id, customer_id)
    return HttpResponse("Task triggered.")