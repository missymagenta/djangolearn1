from django.db import models


class User(models.Model):
    first=models.CharField(max_length=30)
    last=models.CharField(max_length=30)
    email=models.EmailField(max_length=70,blank=True)


    def __str__(self):
        return self.first