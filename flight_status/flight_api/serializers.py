# serializers.py
from rest_framework import serializers
from .models import Customer, Flight, Notification,Booking

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'customer', 'flight', 'booking_date']

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            'id', 'flight_number', 'airline', 'origin_airport_name', 'destination_airport_name',
            'scheduled_departure', 'scheduled_arrival', 'actual_departure',
            'actual_arrival', 'status', 'gate'
        ]

class NotificationSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Notification
        fields = ['id', 'flight', 'customer', 'message', 'sent_at', 'channel']
