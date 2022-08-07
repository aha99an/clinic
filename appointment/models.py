from django.db import models
from patient.models import Patient
from cause.models import Cause
from diagnose.models import Diagnose
from investigation.models import Investigation
from operation.models import Operation
from referrer.models import Referrer
from treatment.models import Treatment 
# Create your models here.
class appointment(models.Model):
    patient= models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True)
    appointmentDate = models.DateField(null=True, blank=True)
    appointmentTypes = (
                        ('N','New Visit'),
                        ('R', 'Repeat'),
                        ('C', 'Consultation'),
                        ('F','Follow up'),
                        ('O','Operative')
    )
    appointmentType = models.CharField(max_length=1,blank=True, choices=appointmentTypes)
    appointmentStatuss= (
                        ('W','Waiting'),
                        ('O', 'On going'),
                        ('D', 'Done'),
                        ('C','Cancel'),
    )
    appointmentStatus = models.CharField(max_length=1,blank=True, choices=appointmentStatuss)


    cause = models.ManyToManyField(
            Cause, blank=True)
    diagnose = models.ManyToManyField(
            Diagnose, blank=True)
    investigation = models.ManyToManyField(
            Investigation, blank=True)
    operation = models.ManyToManyField(
            Operation, blank=True)
    referrer = models.ManyToManyField(
            Referrer, blank=True)
    treatment = models.ManyToManyField(
            Treatment, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return str(self.appointmentDate)
    