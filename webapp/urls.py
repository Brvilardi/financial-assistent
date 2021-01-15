from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name="home"),
    path("accounts/register", views.register, name="register"),
    path("new-expense", views.addExpense, name="addExpense"),
    path("new-expense/post", views.addExpenseHandler, name="addExpenseHandler")
]