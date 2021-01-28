
import time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from webapp import models
from datetime import date
from dateutil.relativedelta import *
import pprint
import json


#Useful functions
def checkIfAuth(request):
    try:
        if not request.user.is_authenticated:
            #To do: return error message
            print("User is not auth")
            return redirect("home")
    except Exception:
        print(f"something went wrong\nuser: {request.user}")

def jsonfy(target):
    newObject = target.__dict__
    print("NEW: ", newObject)          
    try:
        del newObject['_state']
    except Exception:
        pass
    try:
        del newObject['begining']
    except Exception:
        pass
    try:
        del newObject['date']
    except Exception:
        pass
    
    return newObject

def cleanFixedExpenses(fixedExpenses):
    """"
    Returns a dictionary with all fixed expenses from 0 - Jan to 11 - Dec
    """
    today = date.today()
    cleanFixedExpenses = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[]}
    for expense in fixedExpenses:
        #Checks if expense is forever
        if expense.duration == -1:
            month = expense.begining.month
            while(month <= 11):
                cleanFixedExpenses[month].append(jsonfy(expense))
                month += 1

        #populates the first month
        elif expense.begining.year == today.year:
            month = expense.begining.month
            lastDate = expense.begining + relativedelta(months=+expense.duration)
            while(month <= 11):
                #Checks if expend exceed the duration
                if today.replace(month=month) >= lastDate:
                    break
                #Adds the expense on that month
                cleanFixedExpenses[month].append(jsonfy(expense))
                month += 1
    return cleanFixedExpenses

def cleanVariableExpenses(variableExpenses):
    """
    Returns a dictionary with all variable expenses from 0 - Jan to 11 - Dec
    """
    cleanVariableExpenses = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[]}
    for expense in variableExpenses:
        cleanVariableExpenses[expense.date.month].append(jsonfy(expense))
    return cleanVariableExpenses

#-------------------------------------------------------------

# Create your views here.
def index(request):
    print("user: ", request.user.username)
    if request.user.is_authenticated:
        return redirect("home")
    return redirect("login")

def register(request):
    return HttpResponse("<h1>Registration not working yet :(</h1>")

def home(request):
    #Verify if user is auth
    checkIfAuth(request)

    #Gets all expenses of the user
    fixedExpenses = models.FixedExpense.objects.filter(owner=request.user)
    variableExpenses = models.VariableExpense.objects.filter(owner=request.user)  

    #Cleans fixedExpenses for not active expense
    print("Fixed1:")
    print(fixedExpenses)
    cleanedFixedExpenses = cleanFixedExpenses(fixedExpenses.all())#The function is breaking the input, using .all() fixed
    pprint.pprint(cleanedFixedExpenses)
    print("Fixed2:")
    print(fixedExpenses)

    #Cleans variableExpenses for easy front end ingestion
    cleanedVariableExpenses = cleanVariableExpenses(variableExpenses.all())#The function is breaking the input, using .all() fixed
    pprint.pprint(cleanedVariableExpenses)


    
    #Render page with all expenses info
    return render(request, "webapp/home.html", {"username": request.user.username,
                                                "fixedExpenses": fixedExpenses,
                                                "variableExpenses": variableExpenses,
                                                "cleanedFixedExpenses": json.dumps(cleanedFixedExpenses),
                                                "cleanedVariableExpenses": json.dumps(cleanedVariableExpenses)})


def expenseDetails(request, expenseType, expenseId):
    """
        Shows details of specific expense
    """

    #Verify if user is Auth
    checkIfAuth(request)

    #Gets the expense

    if expenseType == 'fixed':
        expense = models.FixedExpense.objects.all().filter(id=expenseId).first()
    elif expenseType == 'variable':
        expense = models.VariableExpense.objects.all().filter(id=expenseId).first()
    else:
        return HttpResponse("expense not found")

    #Checks if user is has access to that expense
    if request.user.id != expense.owner.id:
        return HttpResponse("You don't have privileges")

    #Loads expense data to dictionary
    content = expense.__dict__
    del content['_state']
    del content['owner_id']
    del content['id']
    
    #Loads invisible info
    hiddenContent = {
        'expenseType': expenseType,
        'expenseId': expenseId
        
    }

    #Render page with editable fields for that object
    return render(request, "webapp/expenseDetails.html", {'data': content.items(),
                                                          'hiddenData': hiddenContent.items()})


    print(content)
    
def expenseDetailsHandler(request):
    """
    Handle the expenseDetails POST, for editing expenses
    """
    #Verify if user is auth
    checkIfAuth(request)


    #Verifies if user wants to delete
    try: 
        delete = request.POST['delete'] != None
    except:
        delete = False   
    
    #Gets general expense info
    expenseType = request.POST['expenseType']
    expenseId = request.POST['expenseId']

    #Deletes object if user wants to
    

    #Gets specific expense info and updates or deletes on db
    if expenseType == 'fixed':
        expense = models.FixedExpense.objects.filter(id=expenseId).first()
        if delete:
            expense.delete()
            return HttpResponse(f"Deleted")

        expense.title = request.POST['title']
        expense.value = request.POST['value']
        expense.paymentDay = request.POST['paymentDay']
        expense.description = request.POST['description']
        expense.duration = request.POST['duration']


        expense.save()

    elif expenseType == 'variable':
        expense = models.VariableExpense.objects.filter(id=expenseId).first()
        if delete:
            expense.delete()
            return HttpResponse(f"Deleted")


        expense.title = request.POST['title']
        expense.value = request.POST['value']
        expense.categorie = request.POST['categorie']
        expense.date = request.POST['date']

        expense.save()      

    return HttpResponse(f'Success!! "{expense.title}" updated!')
    



def addExpense(request):
    """"
    fas
    """
    #Verify if user is auth
    checkIfAuth(request)


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