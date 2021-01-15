from django.contrib import admin

from webapp import models

# Register your models here.

admin.site.register(models.FixedExpense)
admin.site.register(models.VariableExpense)
admin.site.register(models.EmailEvents)