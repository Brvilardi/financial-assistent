
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.core.mail import send_mail



# Create your views here.
def index(request):
    print("user: ", request.user.username)
    if request.user.is_authenticated:
        return redirect("home")
    return redirect("login")

def home(request):
    if not request.user.is_authenticated:
        print("User not authenticated")
        return redirect("login")
    return render(request, "webapp/home.html", {"username": request.user.username})

def register(request):
    return HttpResponse("<h1>Registration not working yet :(</h1>")

# def email_test(request):
#     send_mail(
#     'Email test',
#     'This is a Django email test.',
#     'brunovilardibueno@gmail.com',
#     ['brunovilardibueno@gmail.com'],
#     fail_silently=False,
# )