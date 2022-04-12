from .models import Flight, Booking
# 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FlightSerializer, BookingSerializer

@api_view(['GET'])
def show_flights(request, *args, **kwargs):
    flight_model = Flight.objects.all()
    res = []
    for instance in flight_model:
        data = FlightSerializer(instance).data
        res.append(data)
    return Response(res)

@api_view(['GET'])
def upcoming_upcoming(request, *args, **kwargs):
    booking_model = Booking.objects.all()
    res = []
    for instance in booking_model:
        data = BookingSerializer(instance).data
        res.append(data)
    return Response(res)