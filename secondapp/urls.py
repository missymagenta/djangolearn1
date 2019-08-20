from django.urls import path
from secondapp import views
from django.conf.urls import include

urlpatterns = [
    path('', views.users, name='users'),
]