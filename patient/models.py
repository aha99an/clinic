from django.db import models
from datetime import date, datetime
# import datetime
from referrer.models import Referrer
from cause.models import Cause
from django.urls import reverse
from diagnose.models import Diagnose
from investigation.models import Investigation
from treatment.models import Treatment
import appointment.models
import os
# from dateutil import parser
from dateutil.relativedelta import relativedelta

# Create your models here.

GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
class Patient(models.Model):
    name = models.CharField(unique=False, max_length=255)
    phoneNumber = models.CharField(max_length=200, default="0", null=True)
    birthdate = models.DateField(blank=True, null=True)
    @property
    def days(self):
        NOW = datetime.now()
        age = relativedelta(NOW, self.birthdate)
        print(age.days)
        # breakpoint()
        return age.days
    @property
    def months(self):
        NOW = datetime.now()
        age = relativedelta(NOW, self.birthdate)
        return age.months
        # breakpoint()

    @property
    def years(self):
        NOW = datetime.now()
        age = relativedelta(NOW, self.birthdate)
        # breakpoint()
        return age.years
    
        

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
        return reverse('patient_detail', args=[str(self.id)])
    
    def checkNewPatientOrEdit(self):
        return(self.created_at)
    def addAppointmentForNewPatient(self,checkNewPatientOrEdit):
        today = date.today()
        today = int(today.strftime('%Y%m%d'))
        today = str(today)
        todaydate = today[0:4] + "-" + today[4:6] + "-" + today[6:8]
        if checkNewPatientOrEdit == None:
            myappointment = appointment.models.Appointment.objects.create(
                    patient= self,
                    appointmentDate = todaydate,
                    appointmentType =  "New Visit",
                    appointmentStatus= "Waiting"
                    ) 


    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        checkNewPatientOrEdit = self.checkNewPatientOrEdit()
        super(Patient, self).save(*args, **kwargs)
        self.addAppointmentForNewPatient(checkNewPatientOrEdit)


class Attachment(models.Model):
    def content_file_name(instance, filename):
        now = datetime.now()
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










