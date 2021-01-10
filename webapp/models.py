from django.db import models

# Create your models here.

class FixedExpense(models.Model):
    title = models.CharField(max_length=64)
    value = models.FloatField()
    paymentDay = models.IntegerField()
    description = models.TextField()


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

