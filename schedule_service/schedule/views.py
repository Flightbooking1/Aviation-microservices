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
        logger.info("Enter into insert getAll Flights")
        try:
          return self.list(request)
        except Exception as e:
             logger.exception("An error occurred while getAll Flights: %s",str(e))




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

     

 