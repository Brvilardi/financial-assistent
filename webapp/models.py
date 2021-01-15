
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmailEvents(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    date = models.IntegerField()



class FixedExpense(models.Model):
    title = models.CharField(max_length=64)
    value = models.FloatField()
    paymentDay = models.IntegerField()
    description = models.TextField()
    ownear = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - R${self.value} - every {self.paymentDay} by {self.ownear.username}"


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
    ownear = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - R${self.value} - categorie = {self.categorie} by {self.ownear.username}"





