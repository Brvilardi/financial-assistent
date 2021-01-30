import os
import sys
import django
from datetime import date


#  you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planejamentoFinanceiro.settings.local")
django.setup()


from webapp import models
from django.contrib.auth.models import User

def sendNotifications(event, newStatus):
    event.sendSMS()             #Sends a SMS if event has phone number
    event.sendEMAIL()           #sends an email if event has email 
    event.wasSent = newStatus   #updates the status of that event
    event.save()

def run():
    print("sendNotifcation script starting...")
    #Gets the current day
    curDay = date.today().day
    print("Today is: ", curDay)

    #Cleans yesterdays NotificationEvents:
    yesterdayEvents = models.NotificationEvents.objects.all().filter(expense__paymentDay=curDay-1)
    count = 0
    # if yesterdayEvents: #if there was at least 1 event yesterday
    #     for event in yesterdayEvents:
    #         if event.wasSent:
    #             event.wasSent = False
    #             event.save()
    #             count += 1
    #         else:
    #             print(f"Warning! event {event} was not sent yesterday!!\nSending notification for that event...\n")
    #             #sendNotifications(event, False) #activate only if you can garante that run() will run only once a day
                
    # print(f"Total {count} of events updated! - events from paymentDay = {curDay -1}")
    

    #Sends notifications for todays events:
    todayEvents = models.NotificationEvents.objects.all().filter(expense__paymentDay=curDay)
    print("Events: ", todayEvents)
    count = 0
    if todayEvents:
        for event in todayEvents:
            print(f"event: {event} // wasSent: {event.wasSent}")
            if not event.wasSent:
                sendNotifications(event, True)
                count +=1
    print(f"total {count} events sent and updated! - events from paymentDay = {curDay}")