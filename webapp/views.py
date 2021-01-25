
import time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from webapp import models



# Create your views here.
def index(request):
    print("user: ", request.user.username)
    if request.user.is_authenticated:
        return redirect("home")
    return redirect("login")

def register(request):
    return HttpResponse("<h1>Registration not working yet :(</h1>")

def home(request):
    fixedExpenses = models.FixedExpense.objects.filter(owner=request.user)
    variableExpenses = models.VariableExpense.objects.filter(owner=request.user)
    
    # print(fixedExpenses.first())
    if not request.user.is_authenticated:
        print("User not authenticated")
        return redirect("login")
    return render(request, "webapp/home.html", {"username": request.user.username,
                                                "fixedExpenses": fixedExpenses,
                                                "variableExpenses": variableExpenses})


def addExpense(request):
    return render(request, "webapp/addExpense.html", {"username": request.user.username})


def addExpenseHandler(request):
    if request.method == 'GET':
        return HttpResponse("Method not allowed")

    form = request.POST

    if form["expenseType"] == "fixed":
        #Create FixedExpense object
        print("duration: ", form["duration"])
        expense = models.FixedExpense(title=form["title"], value=form["value"], paymentDay=form["paymentDay"], description=form["description"], owner=request.user, duration=int(form['duration']))
        expense.save()

        #Adds expense on alarms
        eventObj = models.NotificationEvents(expense=expense, email=request.user.email)
        eventObj.save()       

    elif form["expenseType"] == "variable":
        expense = models.VariableExpense(title=form["title"], value=form["value"], categorie=form["categorie"], owner=request.user)
        expense.save()

    return HttpResponse("Expense created")







# def email_test(request):
#     send_mail(
#     'Email test',
#     'This is a Django email test.',
#     'brunovilardibueno@gmail.com',
#     ['brunovilardibueno@gmail.com'],
#     fail_silently=False,
# )