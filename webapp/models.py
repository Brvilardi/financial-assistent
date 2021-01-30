import os

from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client
from django.core.mail import send_mail
from datetime import datetime
import boto3

defaultDate = datetime.strptime("01/01/20 13:55:26", '%m/%d/%y %H:%M:%S')

# Create your models here.
class FixedExpense(models.Model):
    title = models.CharField(max_length=64)
    value = models.FloatField()
    paymentDay = models.IntegerField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField(default=-1) #-1== forever
    begining = models.DateField(default=defaultDate)
      

    def __str__(self):
        return f"{self.title} - {self.value} - {self.paymentDay} - {self.owner.username}"

#----------------------------------------------------------------
class VariableExpense(models.Model):
    categories = [
        "Food",
        "Game",
        "Subscription",
        "Random",
        "Electronics",
        "Role",
        "Objects",
        "Health"
    ]


    title = models.CharField(max_length=64)
    value = models.FloatField()
    categorie = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=defaultDate)

    def __str__(self):
        return f"{self.title} - {self.value} - {self.categorie} - {self.date} - {self.owner.username}"

#----------------------------------------------------------------
class NotificationEvents(models.Model):
    expense = models.ForeignKey(FixedExpense, on_delete=models.CASCADE)
    email = models.CharField(max_length=64, default=None, null = True)
    phoneNumber = models.CharField(max_length=64, default=None, null = True)
    wasSent = models.BooleanField(default=False, null = True)

    def __str__(self):
        return f"SMS - to {self.phoneNumber} and/or email to {self.email} about {self.expense}"

    def sendSMS(self):
        try:
            if self.phoneNumber != None:
                # Create an SNS client
                client = boto3.client(
                    "sns",
                    'us-east-1'
                )

                # Send your sms message.
                client.publish(
                    PhoneNumber=self.phoneNumber,
                    Message=f'{self.expense.owner.username}, today is payment day for "{self.expense.title}" on total value of {self.expense.value}'
                )
                

        except Exception:
            print(f"somethin went wrong with SMS {self}")

    def sendEMAIL(self):
        try:
            if self.email != None:
                send_mail(
                f"Payment day for {self.expense.title}!", #subject
                f'{self.expense.owner.username}, today is payment day for "{self.expense.title}" on total value of {self.expense.value}', #body
                'brunovilardibueno@gmail.com', #from
                [self.email], #to
                fail_silently=False,
                )
                print(f"email to {self.expense.owner.username} is sent!")
            else:
                print("Event does not have a email attached, skiping sendEMAIL...")
        except Exception:
            print(f"somethin went wrong with email {self}")

#----------------------------------------------------------------

class UserPhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.phoneNumber}"