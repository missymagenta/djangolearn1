from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def users(request):
    all_users = User.objects.order_by('last')
    return render(request, 'users.html', {'all_users': all_users})