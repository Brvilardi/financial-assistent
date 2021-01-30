from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name="home"),
    path("accounts/register", views.register, name="register"),
    path("accounts/register/handler", views.registerHandler, name="registerHandler"),
    path("new-expense", views.addExpense, name="addExpense"),
    path("new-expense/post", views.addExpenseHandler, name="addExpenseHandler"),
    path("expense-details/<str:expenseType>/<int:expenseId>", views.expenseDetails, name="expenseDetails"),
    path("expenseDetailsHandler", views.expenseDetailsHandler, name="expenseDetailsHandler"),
    path("month/<int:monthIndex>", views.monthDetails, name="monthDetails")
]