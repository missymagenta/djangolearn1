from django.conf.urls import url
from firstapp import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
]