import os
import sys
import django
from datetime import date


#  you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planejamentoFinanceiro.settings.local")
django.setup()


from webapp import models
from django.contrib.auth.models import User

def run():
    print("sendNotifcation script starting...")
    #Gets the current day
    curDay = date.today().day
    # curDay = 25

    #Cleans yesterdays NotificationEvents:
    yesterdayEvents = models.NotificationEvents.objects.all().filter(expense__paymentDay=curDay-1)
    count = 0
    if yesterdayEvents: #if there was at least 1 event yesterday
        for event in yesterdayEvents:
            if event.wasSent:
                event.wasSent = False
                event.save()
                count += 1
            else:
                print(f"Warning! event {event} was not sent yesterday!!")
    print(f"Total {count} of events updated! - events from paymentDay = {curDay -1}")
    

    #Sends notifications for todays events:
    todayEvents = models.NotificationEvents.objects.all().filter(expense__paymentDay=curDay)
    count = 0
    if todayEvents:
        for event in todayEvents:
            # print(f"event: {event} // wasSent: {event.wasSent}")
            if not event.wasSent:
                event.sendSMS()
                event.sendEMAIL()
                event.wasSent = True
                event.save()
                count +=1
    print(f"total {count} events sent and updated! - events from paymentDay = {curDay}")