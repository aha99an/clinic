from django.db import models
from datetime import date
import datetime
from referrer.models import Referrer
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=200, default="0")
    birthdate = models.DateField(null=True, blank=True)

    yORm = 'not set yet'
    @property
    def age(self):
        today = date.today()
        month = today.year - self.birthdate.year
        if month == 0:
            age = today.month - self.birthdate.month
        else:
            age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age
        
    
    def yORm(self):
        today = date.today()
        month = today.year - self.birthdate.year
        if month == 0:
            yORm = 'M'
        else: 
            yORm = 'Y'
        return yORm   
        
          
    #YORM = (
     #   ('Y', 'Year'),
     #   (M', 'Month'),
    #)
    #  = models.CharField(max_length=1, blank=True, choices=YORM, verbose_name="Y/M")
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1,blank=True, choices=GENDER)

    patientAddress = models.CharField(max_length=255)
    referredFrom = models.ForeignKey(
        Referrer, on_delete=models.CASCADE, null=True, blank=True)
    attachment = models.FileField(
        null=True, blank=True, verbose_name="attachment")
    investigation = models.FileField(
        null=True, blank=True, verbose_name="investigation")
    note = models.TextField(blank=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name