from django.db import models
from choices import *
import datetime

# Create your models here.
    
class Owner(models.Model):
    name = models.CharField(max_length=25)
    #password = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, default='mail.dmarkmobile.com')
    contact = models.CharField(max_length=14)

'''
class Client(models.Model):
    name = models.CharField(max_length=25)    
    contact = models.CharField(max_length=14, required=True)
    other_contact = models.CharField(required=False)
'''
    
class Contract(models.Model):
    title = models.CharField(max_length=100)
    signed = models.DateField()
    expiry = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    #client = models.ForeignKey(Client)
    clname = models.CharField(max_length=50)
    clcontact = models.CharField(max_length=14)
    altcontact = models.CharField(max_length=14, blank=True)

    dname = models.CharField(choices=EMPLOYEES, max_length=25, default="")
    dcontact = models.CharField(max_length=14)
    demail = models.CharField(max_length=50)

    #def __unicode__(self):
    #    return u'{0}'.format(self.name)
    

    
class SmsLog(models.Model):
    text = models.CharField(max_length=140)
    receiver = models.CharField(max_length=14)
    tstamp = models.DateTimeField(auto_now_add=True, null=True)
    
    
class Reminder(models.Model):
    #owner = models.ForeignKey(Owner)
    contract = models.ForeignKey(Contract)
    is_set = models.BooleanField(default=False)
    count = models.IntegerField(default=0)













