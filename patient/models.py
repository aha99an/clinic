from django.db import models
from datetime import date
import datetime
from referrer.models import Referrer
from cause.models import Cause
from django.urls import reverse
from diagnose.models import Diagnose
from investigation.models import Investigation
from treatment.models import Treatment
import os
# Create your models here.

GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
YORM = (
        ('Y', 'Years'),
        ('M', 'Months'),
        ('D', 'Days')
    )

class Patient(models.Model):
    name = models.CharField(unique=False, max_length=255)
    phoneNumber = models.CharField(max_length=200, default="0", null=True)
    age= models.CharField(max_length=200, null=False)
    YorM = models.CharField(max_length=1,blank=True, choices=YORM)
    birthdate = models.DateField(blank=True,null=True)
    
    # @property
    # def months(self):
    #     today = date.today()
    #     hismonths = 0
    #     hisYears = today.year - self.birthdate.year
    #     hismonths = today.month - self.birthdate.month
    #     if hismonths < 0:
    #         hismonths = 12 + hismonths
    #     elif hismonths >= 0:
    #         hismonths = hismonths
    #     return hismonths
    # @property
    # def years(self):
    #     today = date.today()
    #     hisYears = today.year - self.birthdate.year
    #     hismonths = today.month - self.birthdate.month
    #     if hismonths < 0:
    #         hisYears = hisYears - 1 
    #     elif hismonths >= 0:
    #         hismonths = hismonths
    #     return hisYears

    gender = models.CharField(max_length=1,blank=True, choices=GENDER)
    patientAddress = models.CharField(max_length=255, null=True)
    patientComplaint = models.CharField(max_length=255, null=True)
    referredFrom = models.ManyToManyField(Referrer, blank=True)
    cause = models.ManyToManyField(Cause, blank=True)
    diagnose = models.ManyToManyField(Diagnose, blank=True)
    investigation = models.ManyToManyField(Investigation, blank=True)
    treatment = models.ManyToManyField(Treatment, blank=True)    
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
            ordering = ('name',)
            
    def __str__(self):
        return self.name

    def get_absolute_url(self):

        today = date.today()
        today = int(today.strftime('%Y%m%d'))
        today = str(today)
        todaydate = today[0:4] + "-" + today[4:6] + "-" + today[6:8] 
        from appointment.models import Appointment
        try:
            myappointment = Appointment.objects.get(
                    patient= self,
                    # appointmentDate = todaydate,
                    appointmentType =  "New Visit"
                    # appointmentStatus= "Waiting"
                    ) 
        except Exception as e :
            myappointment = Appointment.objects.create(
                    patient= self,
                    appointmentDate = todaydate,
                    appointmentType =  "New Visit",
                    appointmentStatus= "Waiting"
                    ) 
            
        return reverse('patient_detail', args=[str(self.id)])
    
    def calculatebirthdate(self):
        today = date.today()
        birthdate = self.birthdate
        if self.YorM == 'Y':
            years= today.year - int(self.age)
            months= '01'
            dayes= '01'
            birthdate = str(years) + "-" + months + "-" + dayes
        elif  self.YorM == 'M':
            if today.month > int(self.age):
                months = today.month - int(self.age)
                years = today.year
                dayes = '01'
                if months == 0:
                    months = 1
                birthdate = str(years) + "-" + str(months) + "-" + dayes
            elif  today.month <= int(self.age):
                years = today.year - 1
                months = 12+ today.month
                months = months - int(self.age)
                dayes = '01'
                birthdate = str(years) + "-" + str(months) + "-" + dayes
        elif  self.YorM == 'D':
                if int(self.age) < today.day:
                    years = today.year
                    months = today.month
                    dayes = today.day - int(self.age)
                    birthdate = str(years) + "-" + str(months) + "-" + str(dayes)
                elif int(self.age) >= today.day:
                    years = today.year
                    months = today.month -1
                    dayes = today.day + 30
                    dayes = dayes - int(self.age)
                    if months == 0:
                        months = 12
                        years = today.year -1

                    birthdate = str(years) + "-" + str(months) + "-" + str(dayes)
        return birthdate

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.birthdate = self.calculatebirthdate()
        super(Patient, self).save(*args, **kwargs)


class Attachment(models.Model):
    def content_file_name(instance, filename):
        now = datetime.datetime.now()
        ext = filename.split('.')[-1]
        orig_filename= filename.split('.')[0]
        filename = "%s_%s.%s" % (orig_filename, now, ext)        
        return os.path.join(str(instance.patient.id), filename)

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="patient_attachments")
    attachment = models.FileField(upload_to=content_file_name,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def snippet_file_name(self):
    if len(self.attachment.name) > 20:
        return "..."+self.attachment.name.rsplit('/', 1)[1][:20]
    else:
        return self.attachment.name










