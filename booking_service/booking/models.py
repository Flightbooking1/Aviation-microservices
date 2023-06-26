from django.db import models

# Create your models here.seat_id
class Seats(models.Model):
    seatId = models.AutoField(primary_key=True,db_column='seat_id')
    scheduleId = models.IntegerField(db_column='schedule_id')
    seatNumber = models.CharField(max_length=45,db_column='seatnumber')
    isAvailable = models.BooleanField(db_column='is_available')
    class Meta:
        db_table='seats'
        managed= False