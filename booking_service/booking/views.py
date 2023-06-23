from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from booking.serializer import SeatSerializer
from booking.models import Seats
import logging

logger = logging.getLogger(__name__)

@api_view(['POST', 'GET'])
def seatSave(request):
    if request.method == 'POST':
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
        
            serializer.save()
            s= Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.info("{}".format(s.data))
            return s
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        seats = Seats.objects.all()
        serializer = SeatSerializer(seats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def seatUpdate(request, sid):
    seat = get_object_or_404(Seats, seatId=sid)

    if request.method == 'GET':
        serializer = SeatSerializer(instance=seat)
        data=Response(serializer.data)
        logger.info("{}".format(data.data))
        return data
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = SeatSerializer(seat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        seat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

