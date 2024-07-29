**Problem Statement :** 

**Flight Status and Notifications :**

A full Decription of the project along with images of the flight status website can be checked at :
https://docs.google.com/document/d/1Eu_4z2ZfXDAwqBgLGgP5UmN3rHtJkVP1iz_LTKBHB7o/edit?usp=sharing

The system is designed to keep passengers informed with real-time flight status updates and notifications. Whether you're tracking your flight or managing multiple flights,the platform ensures you stay updated with the latest information. Below are the key features and technologies used in the system:

**Real-Time Updates:**
Current Status: Display live updates on flight status including delays, cancellations, and gate changes.
Dynamic Refresh: Automatic updates ensure the latest information is always visible without manual refreshes.
**Push Notifications:**
SMS Notifications: Receive instant updates via SMS for critical changes to your flight status.
Email Alerts: Get detailed email notifications about flight status changes.
**Data :** 
A mock data has been created to feed the live dashboard and custom apis have been created to fetch, update, delete the data for flight details, customer details, customer-flight details and notifications to the customer whenever there is a change in flight schedule.
Once real-time data becomes available, the APIs and data models (including JSON and Django models) will be updated to reflect actual flight information. The interface can be updated to showcase real flight information as soon as it is available, providing a seamless experience for users.
**Additional Features:**
Flight Search: Easily search for specific flights and view their current status and any schedule or gate changes.
User Profiles: Manage multiple flight itineraries with personalized settings and notifications.

**Technologies used :** 
For frontend : React, HTML, CSS
For backend : Django, Python
Database : Postgres (locally), db.sqlite3
Notification : RabbitMQ with celery
Miscellaneous : Postman, Git

**For backend :** 

Clone flight_status folder into your local desktop.

Install all the dependencies 

Python app can be run by typing ‘python manage.py runserver’

The app runs and you can see a ui which shows various end points for making get, post, put, update requests. A separate ui can be made for the backend for sending requests, booking flights for users, changing flight details etc. However I have stuck to using django api views for all these changes. The update, delete, get, post requests can be handled by postman as well.
The app runs on http://localhost:8000/ and various endpoints can be used to get details of flights, customers, booking etc.

Separate models have been formed for flights as shown below : 

{ "flight_number": "6E987", "airline": "IndiGo", "origin_airport_name": "Pune Airport", "destination_airport_name": "Cochin International Airport", "scheduled_departure": "2024-08-05T14:00:00", "scheduled_arrival": "2024-08-05T16:30:00", "actual_departure": "2024-08-05T14:00:00", "actual_arrival": "2024-08-05T16:30:00", "status": "on time", "gate": "H4", "changed_gate": "H4" }

For customers details we have : 
{
        "id": 2,
        "name": "mohihin",
        "email": "agarwal.arli@gmail.com",
        "phone": "095604xxxx"
    }
For Bookings we have customer mapping to a particular flight : 
{
    "id": 4,
    "customer": 2,
    "flight": 6,
    "booking_date": "2024-07-29T18:55:42.053936Z"
}
For notifications, this automatically gets filled whenever there are flight changes, it gets updated and the customer associated with the flights gets notified about any changes through mail or sms. These changes happen with the help of rabbitMQ and celery.

For using them make sure you have celery and RabbitMQ installed with all the dependencies.

Move to cd C:\Program Files\RabbitMQ Server\rabbitmq_server-3.13.6\sbin   
Run ‘rabbitmq-plugins enable rabbitmq_management’ on cmd 
‘python -m celery -A flight_status worker --loglevel=info’ on terminal or shell

The app connects with rabbitMQ and soon as an update request is made and changes are made, the associated customer gets a notification.

The settings have the required credentials to be added regarding the password of the sender and the email address. Make those changes to use this service correctly.
The gmail’s original password wont work in most cases, so two step security should be turned on and a customized app password should be created for sending mails through django.

I tried sending mails from mailgun too to have a custom domain and avoid using my personal email id.

All these settings helped me in establishing a notification method in django.


I have created a custom data for flights that can be changed by using postman or django in the build rest api framework ui as per convenience.
Here is the sample flight data I have used : 
[
    {
        "flight_number": "6E123",
        "airline": "IndiGo",
        "origin_airport_name": "Indira Gandhi International Airport",
        "destination_airport_name": "Chhatrapati Shivaji Maharaj International Airport",
        "scheduled_departure": "2024-08-01T10:00:00",
        "scheduled_arrival": "2024-08-01T12:30:00",
        "actual_departure": "2024-08-01T10:00:00",
        "actual_arrival": "2024-08-01T12:30:00",
        "status": "on time",
        "gate": "G12",
        "changed_gate": "G12"
    },
    {
        "flight_number": "6E456",
        "airline": "IndiGo",
        "origin_airport_name": "Kempegowda International Airport",
        "destination_airport_name": "Chennai International Airport",
        "scheduled_departure": "2024-08-01T14:00:00",
        "scheduled_arrival": "2024-08-01T15:30:00",
        "actual_departure": "2024-08-01T14:10:00",
        "actual_arrival": "2024-08-01T15:45:00",
        "status": "delayed",
        "gate": "B3",
        "changed_gate": "B5"
    },
    {
        "flight_number": "6E789",
        "airline": "IndiGo",
        "origin_airport_name": "Netaji Subhas Chandra Bose International Airport",
        "destination_airport_name": "Rajiv Gandhi International Airport",
        "scheduled_departure": "2024-08-02T08:00:00",
        "scheduled_arrival": "2024-08-02T10:45:00",
        "actual_departure": "2024-08-02T08:00:00",
        "actual_arrival": "2024-08-02T10:45:00",
        "status": "on time",
        "gate": "C5",
        "changed_gate": "C5"
    },
    {
        "flight_number": "6E321",
        "airline": "IndiGo",
        "origin_airport_name": "Cochin International Airport",
        "destination_airport_name": "Pune Airport",
        "scheduled_departure": "2024-08-02T12:00:00",
        "scheduled_arrival": "2024-08-02T14:30:00",
        "actual_departure": "2024-08-02T12:10:00",
        "actual_arrival": "2024-08-02T14:45:00",
        "status": "delayed",
        "gate": "A7",
        "changed_gate": "A9"
    },
    {
        "flight_number": "6E410",
        "airline": "IndiGo",
        "origin_airport_name": "Chaudhary Charan Singh International Airport",
        "destination_airport_name": "Sardar Vallabhbhai Patel International Airport",
        "scheduled_departure": "2024-08-03T16:00:00",
        "scheduled_arrival": "2024-08-03T18:15:00",
        "actual_departure": "2024-08-03T16:00:00",
        "actual_arrival": "2024-08-03T18:15:00",
        "status": "on time",
        "gate": "D9",
        "changed_gate": "D9"
    },
    {
        "flight_number": "6E654",
        "airline": "IndiGo",
        "origin_airport_name": "Chhatrapati Shivaji Maharaj International Airport",
        "destination_airport_name": "Indira Gandhi International Airport",
        "scheduled_departure": "2024-08-03T20:00:00",
        "scheduled_arrival": "2024-08-03T22:30:00",
        "actual_departure": "2024-08-03T20:00:00",
        "actual_arrival": "2024-08-03T22:30:00",
        "status": "on time",
        "gate": "E11",
        "changed_gate": "E13"
    },
    {
        "flight_number": "6E789",
        "airline": "IndiGo",
        "origin_airport_name": "Chennai International Airport",
        "destination_airport_name": "Kempegowda International Airport",
        "scheduled_departure": "2024-08-04T06:00:00",
        "scheduled_arrival": "2024-08-04T07:30:00",
        "actual_departure": "2024-08-04T06:10:00",
        "actual_arrival": "2024-08-04T07:35:00",
        "status": "delayed",
        "gate": "F2",
        "changed_gate": "F3"
    },
    {
        "flight_number": "6E101",
        "airline": "IndiGo",
        "origin_airport_name": "Rajiv Gandhi International Airport",
        "destination_airport_name": "Netaji Subhas Chandra Bose International Airport",
        "scheduled_departure": "2024-08-04T10:00:00",
        "scheduled_arrival": "2024-08-04T12:45:00",
        "actual_departure": "2024-08-04T10:00:00",
        "actual_arrival": "2024-08-04T12:45:00",
        "status": "on time",
        "gate": "G8",
        "changed_gate": "G9"
    },
    {
        "flight_number": "6E987",
        "airline": "IndiGo",
        "origin_airport_name": "Pune Airport",
        "destination_airport_name": "Cochin International Airport",
        "scheduled_departure": "2024-08-05T14:00:00",
        "scheduled_arrival": "2024-08-05T16:30:00",
        "actual_departure": "2024-08-05T14:00:00",
        "actual_arrival": "2024-08-05T16:30:00",
        "status": "on time",
        "gate": "H4",
        "changed_gate": "H4"
    },
    {
        "flight_number": "6E1234",
        "airline": "IndiGo",
        "origin_airport_name": "Sardar Vallabhbhai Patel International Airport",
        "destination_airport_name": "Chaudhary Charan Singh International Airport",
        "scheduled_departure": "2024-08-05T18:00:00",
        "scheduled_arrival": "2024-08-05T20:15:00",
        "actual_departure": null,
        "actual_arrival": null,
        "status": "cancelled",
        "gate": "I6",
        "changed_gate": "I8"
    }
]


Similarly customers data has been created and customer details have been mapped to flight by using a foreign key relation in the models.py.

This is a sample data and sample end points have been created. Once we have real time data formats and json structures, we can make the necessary changes to the files and ui.

**Explanation for django files and models :** 
**1. views.py**
This file contains view classes and functions that handle HTTP requests and interact with the database.
CustomerViewSet: Handles CRUD operations for Customer objects. It uses Django REST Framework's ModelViewSet to provide a full set of RESTful API endpoints for customer data.
FlightViewSet: Manages CRUD operations for Flight objects with RESTful API endpoints.
BookingViewSet: Provides RESTful API endpoints for Booking objects, allowing CRUD operations.
NotificationViewSet: Manages RESTful API endpoints for Notification objects. Works with RabbitMQ.
send_test_email: A view function that sends a test email using Django's send_mail function. This is useful for testing email functionality.
test_task: A view function that triggers a Celery task to send a test notification. It demonstrates how to enqueue background tasks using Celery.
**2. models.py**
This file defines the data models for the application.
Customer: Represents customers with fields for their name, email, and phone number.
Flight: Represents flight information including flight number, airline, origin, destination, scheduled and actual departure/arrival times, status, and gate information.
Booking: Represents a booking, linking a customer to a flight and recording the booking date.
Notification: Represents a notification sent to a customer regarding a flight. 
**3. urls.py**
This file maps URLs to the corresponding view functions or viewsets.
router: An instance of DefaultRouter that automatically creates URL patterns for the API endpoints defined in the viewsets (CustomerViewSet, FlightViewSet, BookingViewSet, and NotificationViewSet).
urlpatterns: A list of URL patterns. It includes:
The routes for the REST API endpoints (using the router).
A route to trigger the send_test_email function.
**4. serializers.py** 
Serializers.py convert complex data types (like Django models) into JSON and vice versa. 
**5. tasks.py, celery.py, signals.py**
It contains Celery tasks, including send_notification_task, which is used in the test_task view function to send notifications asynchronously.
This Django project is designed to manage and provide real-time flight status updates, notifications, and bookings. It integrates various features including email notifications and task handling with Celery.


**For Frontend :** 

Download or clone the file.

Run npm install on the terminal  

Move to the flight_status_frontend directory by cd  flight_status_frontend if you are under the folder Flight_frontend.

After coming to this location type npm start.

The react js project can be found at http://localhost:3000/

Once the port is live you can get live updates about flights, gate changes, reschedule, postpone, cancel etc. A customer can search for a particular flight as well to know if any changes in the schedule have taken place or not. This dashboard can serve as an unique tool for the airports or flights to keep a track of flight changes which the customer can see easily. 


