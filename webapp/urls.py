from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name="home"),
    path("accounts/register", views.register, name="register"),
    path("email_test", views.email_test, name="email_test")
]