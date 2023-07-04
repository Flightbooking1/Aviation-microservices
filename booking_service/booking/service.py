from .views import *
from django.db import connection

class BookingHistoryService:
    def saveBh(self,args):
        logget.info("Entered into saveBh")
        logget.info("BookingHistoryService.saveBh ========= {} ".format(args))
        
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM `booking-module`.booking_history WHERE date='{args.date}'and schedule_id='{args.schedule_id}' ;")
        result = cursor.fetchone()
    
        logget.info(" =========== {}".format(result))
        try:
            bk = BookingHistory.objects.get(schedule_id=args.schedule_id, date=args.date)
            logget.info(" =========== ************************** {}".format(bk))
            bhSerial= BookingHistorySerializer(args)
            logget.info(">>>>>>>>>>>>>>>>>. {}".format(bk.available_tickets - bhSerial.data['no_of_tickets_booked']))
            bhv = BookingHistory.objects.get(booking_history_id=bk.booking_history_id)
            bhv.no_of_tickets_booked = bk.no_of_tickets_booked + bhSerial.data['no_of_tickets_booked']
            bhv.available_tickets = bk.available_tickets - bhSerial.data['no_of_tickets_booked']
            bhv.save()
            logget.info("  --------------------------- {}".format(bhv))
        except BookingHistory.DoesNotExist:
            logget.info("Booking history not found for the provided schedule_id and date.")
            bhSerial= BookingHistorySerializer(args)
           
            bhv =BookingHistory.objects.create(
                no_of_tickets_booked= bhSerial.data['no_of_tickets_booked'],
                date = bhSerial.data['date'],
                days_left= bhSerial.data['days_left'],
                available_tickets=bhSerial.data['available_tickets'],
                schedule_id=bhSerial.data['schedule_id']
            )
          
            logget.info(bhv)
           
        

        # if result is None:
        #     bhSerial= BookingHistorySerializer(args)
        #     print("................................................................")
        #     print(bhSerial.data)
        #     print("................................................................")
        #     # booking_history_id, no_of_tickets_booked, date, available_tickets, schedule_id, days_left
        #     # {'booking_history_id': None, 'no_of_tickets_booked': 2, 'date': '2023-06-29', 'available_tickets': 35,
        #     #  'schedule_id': 3, 'days_left': 11}
        #     bhv =BookingHistory.objects.create(
        #         no_of_tickets_booked= bhSerial.data['no_of_tickets_booked'],
        #         date = bhSerial.data['date'],
        #         days_left= bhSerial.data['days_left'],
        #         available_tickets=bhSerial.data['available_tickets'],
        #         schedule_id=bhSerial.data['schedule_id']
        #     )
        #     print("................................................................")
        #     print(bhv)
        #     print("................................................................")

        # else:
        #     bhSerial= BookingHistorySerializer(args)
        #     print("{} , {} ,{}".format(result[1], result[3], result[2]))
        #     bhv = BookingHistory.objects.get(booking_history_id=result[0])
        #     bhv.no_of_tickets_booked = result[1] + bhSerial.data['no_of_tickets_booked']
        #     bhv.available_tickets = result[3] - bhSerial.data['no_of_tickets_booked']
        #     bhv.save()
        #     print("  --------------------------- {}".format(bhv))
    
    def deleteBh(self,schedule_id, no_of_tickets_canceled ):
        logget.info("Entered into deleteBh ")
        logget.info(schedule_id)
        try:
            bk = BookingHistory.objects.get(schedule_id=schedule_id, date=today_data.today())
            
            logget.info(bk)
        except BookingHistory.DoesNotExist as e:
            logget.info("While Deleting Booking Histort = {}".format(e))

        