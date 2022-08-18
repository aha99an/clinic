from django.db import models
from datetime import date
import datetime
from referrer.models import Referrer
from cause.models import Cause
from django.urls import reverse
from diagnose.models import Diagnose
from investigation.models import Investigation
from treatment.models import Treatment
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=200, default="0")
    birthdate = models.DateField(null=True, blank=True)

    yORm = 'not set yet'
    @property
    def years(self):
        today = date.today()
        hisYears = today.year - self.birthdate.year
        hismonths = today.month - self.birthdate.month
        if hismonths < 0:
            hisYears = hisYears - 1 
        elif hismonths >= 0:
            hismonths = hismonths
        return hisYears

    def months (self):
        today = date.today()
        hisYears = today.year - self.birthdate.year
        hismonths = today.month - self.birthdate.month
        if hismonths < 0:
            hismonths = 12 + hismonths
        elif hismonths >= 0:
            hismonths = hismonths
        return hismonths
  
        
          
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
    referredFrom = models.ForeignKey(Referrer, on_delete=models.CASCADE, null=True, blank=True)
    cause = models.ManyToManyField(Cause, blank=True)
    diagnose = models.ManyToManyField(Diagnose, blank=True)
    investigation = models.ManyToManyField(Investigation, blank=True)
    treatment = models.ManyToManyField(Treatment, blank=True)    
    attachment = models.FileField(null=True, blank=True, verbose_name="attachment")
    note = models.TextField(blank=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])