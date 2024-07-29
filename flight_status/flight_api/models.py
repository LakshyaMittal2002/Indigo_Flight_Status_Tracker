# models.py
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    airline = models.CharField(max_length=50)
    origin_airport_name = models.CharField(max_length=100)
    destination_airport_name = models.CharField(max_length=100)
    scheduled_departure = models.DateTimeField()
    scheduled_arrival = models.DateTimeField()
    actual_departure = models.DateTimeField(null=True, blank=True)
    actual_arrival = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('on time', 'On Time'), ('delayed', 'Delayed'), ('cancelled', 'Cancelled'),('Before Time','before time')])
    gate = models.CharField(max_length=10, null=True, blank=True)
    Changed_gate = models.CharField(max_length=10, null=True, blank=True)

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    flight = models.ForeignKey(Flight, related_name='notifications', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    channel = models.CharField(max_length=20, choices=[('sms', 'SMS'), ('email', 'Email'), ('app', 'App')])




