from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import  ListModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin,UpdateModelMixin
from  .models import *
from .serializers import *
import logging
logger=logging.getLogger(__name__)

# Create your views here.
class AirportInsertandGettingall(GenericAPIView,CreateModelMixin,ListModelMixin):
     queryset = Airport.objects.all()
     serializer_class=AirportSerializer
     def post(self,request):
          logger.info("Enter into insert Airport")
          try:
               return self.create(request)
          except Exception as e:
            logger.exception("An error occurred while saving a Airport: %s",str(e))
         
     def get(self,request):
        logger.info("Enter into insert getAll Airports")
        try:
          return self.list(request)
        except Exception as e:
             logger.exception("An error occurred while getAll Airports: %s",str(e))



class updateAndDeleteAndRetraiveByID(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
     queryset=Airport.objects.all()
     serializer_class=AirportSerializer
     def put(self,request,**kwargs):
          logger.info("Enter into update Airport")
          try:
               return self.update(request,**kwargs)
          except Exception as e:
               logger.exception("An error occurred while updating a Airport: %s",str(e))

     def delete(self,request,**kwargs):
          logger.info("Enter into delete Airport")
          try:
               return self.destroy(request,**kwargs)
          except Exception as e:
               logger.exception("An error occurred while deleting a Airport: %s",str(e))

<<<<<<< Updated upstream
     def get(self,request,**kwargs):
          logger.info("Enter into getById Airport")
          try:
               return self.retrieve(request,**kwargs)
          except Exception as e:
               logger.exception("An error occurred while getById a Airport: %s",str(e))
               
class FlightInsertandGettingall(GenericAPIView,CreateModelMixin,ListModelMixin):
     queryset = Flight.objects.all()
     serializer_class=FlightSerializer
     def post(self,request):
          logger.info("Enter into insert Flight")
          try:
               return self.create(request)
          except Exception as e:
            logger.exception("An error occurred while saving a Flight: %s",str(e))
          
     def get(self,request):
=======
    def get(self, request, **kwargs):
        logger.info("Enter into getById Airport")
        try:
            return self.retrieve(request, **kwargs)
        except Exception as e:
            logger.exception(
                "An error occurred while getById a Airport: %s", str(e))
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PATCH'])
def patchAirport(request, id):
    logger.info("Enter into patch Airport")
    try:
        airport = Airport.objects.get(id=id)
    except Airport.DoesNotExist:
        return Response({'error': 'Airport not found'}, status=status.HTTP_404_NOT_FOUND)

    if (airport.status == "Active"):
        # Assign the field value "InActive" to the desired field
        airport.status = "InActive"
    elif (airport.status == "InActive"):
        airport.status = "Active"
    else:
        airport.status = "Active"
    try:
        # Save the updated airport object
        airport.save()

        # Return the serialized data in the response
        serializer = AirportSerializer(airport)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ---------------------Flight Operations-----------------------------


class FlightInsertandGettingall(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def post(self, request):
        logger.info("Enter into insert Flight")
        try:
            return self.create(request)
        except Exception as e:
            logger.exception(
                "An error occurred while saving a Flight: %s", str(e))
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
>>>>>>> Stashed changes
        logger.info("Enter into insert getAll Flights")
        try:
          return self.list(request)
        except Exception as e:
             logger.exception("An error occurred while getAll Flights: %s",str(e))




<<<<<<< Updated upstream
class FlightupdateAndDeleteAndRetraiveByID(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
     queryset=Flight.objects.all()
     serializer_class=FlightSerializer
     def put(self,request,**kwargs):
          logger.info("Enter into update Flight")
          try:
               return self.update(request,**kwargs)
          except Exception as e:
               logger.exception("An error occurred while updating a Flight: %s",str(e))
     def delete(self,request,**kwargs):
          logger.info("Enter into delete Flight")
          try:
               return self.destroy(request,**kwargs)
          except Exception as e:
               logger.exception("An error occurred while deleting a Flight: %s",str(e))
     def get(self,request,**kwargs):
          logger.info("Enter into getById Flight")
          try:
               return self.retrieve(request,**kwargs)
          except Exception as e:
               logger.exception("An error occurred while getById a Flight: %s",str(e))

@api_view(['POST'])
def inserting(request):
    logger.info(request.data)
    airport_data=Airport.objects.all()
    logger.info("getting %s",airport_data)
    data=airport_data
    print(data)
    source_airport_data = request.data.get('source_airport')
    print(source_airport_data,"id not %s")
    source_airport_id = source_airport_data.get('id')
    print(source_airport_id,"id not %s")
    serilizer=ScheduleSerializer(data=request.data,)
    if serilizer.is_valid():
          logger.info("Enter into inserting schedule")
          serilizer.save()
          return Response(serilizer.data)
    else:
          return Response("not saved")
=======
@api_view(['PATCH'])
def patchFlight(request, id):
    logger.info("Enter into patch Flight")
    try:
        flight = Flight.objects.get(id=id)
    except Flight.DoesNotExist:
        return Response({'error': 'Flight not found'}, status=status.HTTP_404_NOT_FOUND)

    # Assign the field value "InActive" to the desired field
    if (flight.status == "Active"):
        flight.status = "InActive"
    elif (flight.status == "InActive"):
        flight.status = "Active"
    else:
        flight.status = "Active"
    try:
     # Save the updated Flight object
        flight.save()

        # Return the serialized data in the response
        serializer = FlightSerializer(flight)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#  -----------------Schedule Operations------------------------


@api_view(['POST'])
def inserting(request):
    try:
        logger.info(request.data)
        #    airport_data = Airport.objects.all()
        #    logger.info("getting %s", airport_data)
        #    data = airport_data
        #    logger.info(data)
        #    source_airport_data = request.data.get('source_airport')
        #    logger.info(source_airport_data, "id not %s")
        #    source_airport_id = source_airport_data.get('id')
        #    logger.info(source_airport_id, "id not %s")
        serilizer = ScheduleSerializer(data=request.data,)
        if serilizer.is_valid():
            logger.info("Enter into inserting schedule")
            serilizer.save()
            return Response(serilizer.data)
        else:
            logger.exception(
                "An error occurred while saving a Schedule: %s")
            return Response({'error not saved'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.exception(
            "An error occurred while getting request: %s", str(e))
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

>>>>>>> Stashed changes

@api_view(['GET'])
def gettingData(request):
    allData=Schedule.objects.all()
    serializer=ScheduleSerializer(data=allData,many=True)
    serializer.is_valid()
    return Response(serializer.data) 

@api_view(['GET'])
def getById(request, id):
    try:
        schedule = Schedule.objects.get(id=id)
        serializer = ScheduleRetrevieSerializer(instance=schedule)
        return Response(serializer.data)
    except Schedule.DoesNotExist:
        logger.error(f"Schedule with id {id} does not exist.")
        return Response(status=404)

@api_view(['PUT'])
def updateSchedule(request,id):
     print(request.data)
     up_data=Schedule.objects.get(id=id)
     logger.info("update schedule",up_data)
     serializer = SchedulesSerializer(instance=up_data,data=request.data)
     serializer.is_valid()
     serializer.save()
     return Response(serializer.data) 

@api_view(['DELETE'])
def deleteSchedule(request,id):
     try:
          del_data= Schedule.objects.get(id=id)
          logger.info("delete schedule", del_data)
          del_data.delete()
          return Response("deleted succesfully")
     except:
          logger.error(f"Schedule with id {id} does not exist.")
          return Response(status=404)

     

<<<<<<< Updated upstream
 
=======
@api_view(['PATCH'])
def patchSchedule(request, id):
    logger.info("Enter into insert Schedule")
    try:
        schedule = Schedule.objects.get(id=id)
    except Schedule.DoesNotExist:
        return Response({'error': 'Schedule not found'}, status=status.HTTP_404_NOT_FOUND)

    # Assign the field value "InActive" to the desired field
    
    if (schedule.status == "Active"):
        schedule.status = "InActive"
    elif (schedule.status == "InActive"):
        schedule.status = "Active"
    else:
        schedule.status = "Active"
    try:
        # Save the updated Schedule object
        schedule.save()

        # Return the serialized data in the response
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PATCH'])
def patchAvailableTickets(request, id, available_seats):
    logger.info("Entered into update avilable_tickets in  Schedule ")
    logger.info("  get the available seats {}".format(
        request.data.get('available_seats')))

    try:
        schedule = Schedule.objects.get(id=id)

        logger.info(" arrival time{}".format(schedule.arrival_time))

    except Schedule.DoesNotExist:
        logger.info("Schedule not found")
        return Response({'error': 'Schedule not found'}, status=status.HTTP_404_NOT_FOUND)

    # Assign the field value available_seats to the desired field
    schedule.available_seats = available_seats
    try:
        logger.info("enter into try block of patch {}".format(
            schedule.available_seats))
        # Save the updated Schedule object
        schedule.save()
        logger.info("saved successfully schedule")
        # Return the serialized data in the response
        serializer = ScheduleSerializer(schedule)
        logger.info("serialized data {}".format(serializer.data))
        return Response(serializer.data)
    except Exception as e:
        logger.info("Exception in patch for availableSeats")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
>>>>>>> Stashed changes
