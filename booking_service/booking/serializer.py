from rest_framework import serializers
from booking.models import Seats

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = ['scheduleId', 'seatNumber', 'isAvailable']

