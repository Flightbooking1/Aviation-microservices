from django.db import models

class Booking(models.Model):
    bookingId = models.AutoField(primary_key=True, db_column='booking_id')
    email = models.EmailField(max_length=70, db_column='email')
    journeyDate = models.DateField(db_column='journey_date')
    bookingDate = models.CharField(max_length=45, db_column='booking_date')
    status = models.CharField(max_length=45, db_column='status')
    pnrNumber = models.CharField(max_length=45, db_column='pnr_number')
    scheduleId = models.CharField(max_length=45, db_column='schedule_id')

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        managed = False
        db_table = 'booking'


        

class Transaction(models.Model):
    transactionId = models.AutoField(primary_key=True, db_column='transaction_id')
    transactionStatus = models.CharField(max_length=45, db_column='transaction_status')
    transactionType = models.CharField(max_length=45, db_column='transaction_type')
    amount = models.FloatField()
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, db_column='booking_id')
    

    def __str__(self) -> str:
        return self.amount
    
    class Meta:
        managed = False
        db_table = 'transaction'

class Passenger(models.Model):
    passengerId = models.AutoField(primary_key=True, db_column='passenger_id')
    passengerName = models.CharField(max_length=45, db_column='passenger_name')
    passengerAge = models.IntegerField(db_column='passenger_age')
    passengerAadhar = models.CharField(max_length=45, db_column='passenger_aadhar')
    passengerStatus = models.CharField(max_length=45, db_column='passenger_status')
    seatNumber = models.CharField(max_length=45, db_column='seat_number')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, db_column='booking_id_ref')


    def __str__(self) -> str:
        return self.passengerName

    class Meta:
        managed = False
        db_table = 'passengers'

