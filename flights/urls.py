from django.urls import path
from .views import show_flights, upcoming_upcoming

urlpatterns = [
    path('flights-list/', show_flights, name="flights-list"),
    path('bookings-list/', upcoming_upcoming, name="bookings-list"),
]
