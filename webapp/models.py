import os

from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client
from django.core.mail import send_mail

# Create your models here.
class FixedExpense(models.Model):
    title = models.CharField(max_length=64)
    value = models.FloatField()
    paymentDay = models.IntegerField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField(default=-1) #-1== forever
    begining = models.DateTimeField(auto_now_add=True, null=True)

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
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.value} - {self.categorie} - {self.date} - {self.owner.username}"

#----------------------------------------------------------------
class NotificationEvents(models.Model):
    expense = models.ForeignKey(FixedExpense, on_delete=models.CASCADE)
    email = models.CharField(max_length=64, default=None, null = True)
    phoneNumber = models.CharField(max_length=64, default=None, null = True)
    wasSent = models.BooleanField(default=False, null = True)

    def __str__(self):
        return f"SMS - to {self.phoneNumber} about {self.expense}"

    def sendSMS(self):
        if self.phoneNumber != None:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body = f'{self.expense.owner.username}, today is payment day for "{self.expense.title}" on total value of {self.expense.value}',
                                        from_ = os.environ['TWILIO_PHONE_NUMBER'],
                                        to = self.phoneNumber
                                    )
            print(f"Sms {message.sid} to {self.expense.owner.username} is sent!")
        else:
            print("Event does not have a phoneNumber attached, skiping sendSMS...")

    def sendEMAIL(self):
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


