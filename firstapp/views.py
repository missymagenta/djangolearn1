from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me': "I am coming from views.py"}
    return render(request, 'firstapp.html', context=my_dict)
