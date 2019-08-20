import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','learning.settings')


import django
django.setup()

import random
from firstapp.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    '''
    create n entries of dates accessed
    '''

    for entry in range(N):

        # get topic for entry with get topic function
        top = add_topic()

        # create fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create new Webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create fake access record for that page
        accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('populating database... please wait')
    populate(20)
    print('populating complete')
