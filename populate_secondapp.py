import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learning.settings')


import django
django.setup()

import random
from secondapp.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    create n entries of dates accessed
    '''

    for entry in range(N):

        # create fake data for entry
        fake_first = fakegen.name()
        fake_last = fakegen.name()
        fake_email = fakegen.email()

        #create new Webpage entry
        user = User.objects.get_or_create(first=fake_first,last=fake_last,email=fake_email)[0]


if __name__ == '__main__':
    print('populating database... please wait')
    populate(20)
    print('populating complete')
