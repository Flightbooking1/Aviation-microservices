from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from booking.serializer import *
from booking.models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import  ListModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin,UpdateModelMixin
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
    
# -------------------------------------Transaction Operations--------------------------------------

class TransactionInsertandGettingall(GenericAPIView,CreateModelMixin,ListModelMixin):
     queryset = Transaction.objects.all()
     serializer_class=TransactionSerializer
     def post(self,request):
          return self.create(request)
     def get(self,request):
        return self.list(request)

class TransactionUpadateAndDeleteAndRetraiveByID(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
     queryset=Transaction.objects.all()
     serializer_class=TransactionSerializer
     def put(self,request,**kwargs):
          return self.update(request,**kwargs)
     def delete(self,request,**kwargs):
          return self.destroy(request,**kwargs)
     def get(self,request,**kwargs):
          return self.retrieve(request,**kwargs)
     
@api_view(['GET'])
def getTransactionByBookingId(request, bookingId):
     transaction = Transaction.objects.filter(booking=bookingId)
     transactionSerializer = TransactionSerializer(instance = transaction)
     return Response(transactionSerializer.data, status=status.HTTP_200_OK)
     
# -------------------------------------Passengers Operations--------------------------------------

class PassengerInsertandGettingall(GenericAPIView,CreateModelMixin,ListModelMixin):
     queryset = Passenger.objects.all()
     serializer_class=PassengerSerializer
     def post(self,request):
          return self.create(request)
     def get(self,request):
        return self.list(request)
     
class PassengerUpadateAndDeleteAndRetraiveByID(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
     queryset=Passenger.objects.all()
     serializer_class=PassengerSerializer
     def put(self,request,**kwargs):
          return self.update(request,**kwargs)
     def delete(self,request,**kwargs):
          return self.destroy(request,**kwargs)
     def get(self,request,**kwargs):
          return self.retrieve(request,**kwargs)
     
@api_view(['GET'])
def getPassengerByBookingId(request, bookingId):
     passengers = Passenger.objects.filter(booking=bookingId)
     passengerSerializer = PassengerSerializer(data = passengers, many=True)
     passengerSerializer.is_valid()
     return Response(passengerSerializer.data, status=status.HTTP_200_OK)
# -------------------------------------Booking Operations--------------------------------------

@api_view(['POST','GET'])
def booking(request):
     if request.method == 'POST':
          serializer = BookingSerializer(data = request.data)
          if serializer.is_valid():
               serializer.save()
               booking_id = serializer.instance.bookingId
               bookings = Booking.objects.get(bookingId = booking_id)
               retriveSerializer = BookingRetrieveSerializer(instance = bookings)
               transaction = Transaction.objects.get(booking = booking_id)
               transactionSerializer = TransactionSerializer(instance = transaction)
               passengers = Passenger.objects.filter(booking=booking_id)
               passengerSerializer = PassengerSerializer(data = passengers, many=True)
               passengerSerializer.is_valid()
               return Response([retriveSerializer.data,transactionSerializer.data,passengerSerializer.data], status= status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     else:
          booking = Booking.objects.all()
          serializer = BookingRetrieveSerializer(data=booking, many=True)
          serializer.is_valid()
          print(serializer.data)
          return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT','GET','DELETE'])
def getBooking(request,id):
     if request.method =='PUT':
          booking = Booking.objects.get(bookingId=id)
          serializer = BookingRetrieveSerializer(booking, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     elif request.method =='GET':
          booking = Booking.objects.get(bookingId=id)
          serializer = BookingRetrieveSerializer(instance = booking)
          return Response(serializer.data, status=status.HTTP_200_OK)
     else:
          booking = Booking.objects.get(bookingId=id)
          transaction = Transaction.objects.get(booking = id)
          transaction.delete()
          passengers = Passenger.objects.filter(booking= id)
          for passenger in passengers:
               passenger.delete()
          booking.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)


