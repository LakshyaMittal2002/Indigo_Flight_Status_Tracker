# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, FlightViewSet, NotificationViewSet,BookingViewSet,send_test_email,test_task

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('send-test-email/', send_test_email, name='send_test_email'),
    path('test-task/', test_task, name='test_task'),
]
