from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic,Webpage,AccessRecord

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')

    date_dict = {'access_records': webpages_list}
    return render(request, 'firstapp.html', date_dict)
