# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Booking(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=70)
    journey_date = models.DateField()
    booking_date = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    pnr_number = models.CharField(unique=True, max_length=45)
    schedule_id = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'booking'


class BookingHistory(models.Model):
    booking_history_id = models.IntegerField(primary_key=True)
    no_of_tickets_booked = models.IntegerField()
    date = models.DateField()
    available_tickets = models.IntegerField()
    schedule_id = models.IntegerField()
    days_left = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'booking_history'


class Passengers(models.Model):
    passenger_id = models.IntegerField(primary_key=True)
    passenger_name = models.CharField(max_length=45)
    passenger_age = models.IntegerField()
    passenger_aadhar = models.CharField(max_length=45)
    passenger_status = models.CharField(max_length=45)
    seat_number = models.CharField(max_length=45)
    booking_id_ref = models.ForeignKey(Booking, models.DO_NOTHING, db_column='booking_id_ref')

    class Meta:
        managed = False
        db_table = 'passengers'


class Seats(models.Model):
    seat_id = models.IntegerField(primary_key=True)
    schedule_id = models.IntegerField()
    seatnumber = models.CharField(unique=True, max_length=45)
    is_available = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seats'


class Transaction(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    transaction_status = models.CharField(max_length=45)
    transaction_type = models.CharField(max_length=45)
    amount = models.FloatField()
    booking = models.ForeignKey(Booking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'transaction'
