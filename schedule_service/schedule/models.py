# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Flight(models.Model):
    flight_number = models.IntegerField()
    seating_capacity = models.IntegerField()
    status = models.CharField(max_length=45)
    class Meta:
        db_table = 'flight'

class Airport(models.Model):
    airport_name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    class Meta:
        db_table = 'airport'
class Schedule(models.Model):
    source_airport = models.ForeignKey(Airport, models.DO_NOTHING, db_column='source_airport', related_name='source_schedules')
    destination_airport = models.ForeignKey(Airport, models.DO_NOTHING, db_column='destination_airport', related_name='destination_schedules')
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    available_seats = models.IntegerField()
    base_price = models.FloatField()
    flight = models.ForeignKey(Flight, on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'schedule'
