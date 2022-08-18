from django.db import models
from django.urls import reverse
from patient.models import Patient 
from operation.models import Operation

# Create your models here.
class Appointment(models.Model):
    patient= models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    appointmentDate = models.DateField(null=True, blank=True)
    appointmentTypes = (
                        ('New Visit','New Visit'),
                        ('Repeat', 'Repeat'),
                        ('Consultation', 'Consultation'),
                        ('Follow up','Follow up'),
                        ('Operative','Operative')
    )
    appointmentType = models.CharField(max_length=20,blank=True, choices=appointmentTypes)
    appointmentStatuss = (
                        ('Waiting','Waiting'),
                        ('On going', 'On going'),
                        ('Done', 'Done'),
                        ('Cancel','Cancel'),
    )
    appointmentStatus = models.CharField(max_length=20,blank=True, choices=appointmentStatuss)

    operation = models.ManyToManyField(Operation, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 
    def __str__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse('appointments')