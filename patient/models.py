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
# from django.contrib.auth.models import User

# User._meta.get_field('username')._unique = False
GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
class Patient(models.Model):
    # id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(unique=True, max_length=255)
    phoneNumber = models.CharField(max_length=200, default="0", null=True)
    birthdate = models.DateField(blank=True)
    @property
    def months(self):
        today = date.today()
        hismonths = 0
        hisYears = today.year - self.birthdate.year
        hismonths = today.month - self.birthdate.month
        if hismonths < 0:
            hismonths = 12 + hismonths
        elif hismonths >= 0:
            hismonths = hismonths
        return hismonths
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

    gender = models.CharField(max_length=1,blank=True, choices=GENDER)
    patientAddress = models.CharField(max_length=255, null=True)
    patientComplaint = models.CharField(max_length=255, null=True)
    referredFrom = models.ManyToManyField(Referrer, blank=True)
    cause = models.ManyToManyField(Cause, blank=True)
    diagnose = models.ManyToManyField(Diagnose, blank=True)
    investigation = models.ManyToManyField(Investigation, blank=True)
    treatment = models.ManyToManyField(Treatment, blank=True)    
    # attachment = models.FileField(null=True, blank=True, verbose_name="attachment")
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
        print(todaydate)
        myappointment, _ = Appointment.objects.get_or_create(
                patient= self,
                appointmentDate = todaydate,
                appointmentType =  "New Visit",
                appointmentStatus= "Waiting"
                ) 
        
        return reverse('patient_detail', args=[str(self.id)])
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()

        super(Patient, self).save(*args, **kwargs)



    # def addAppointmentAutomatic(self):
    #     today = date.today()
    #     today = int(today.strftime('%Y%m%d'))
    #     today = str(today)
    #     todaydate = today[0:4] + "-" + today[4:6] + "-" + today[6:8] 
    #     from appointment.models import Appointment
    #     print(todaydate)
    #     myappointment, _ = Appointment.objects.get_or_create(
    #             patient= self,
    #             appointmentDate = todaydate,
    #             appointmentType =  "New Visit",
    #             appointmentStatus= "Waiting"
    #             ) 


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


# now = datetime.datetime.now()










