from django.db import models
from django.urls import reverse
from patient.models import Patient 
from operation.models import Operation
from followup.models import Followup
from newVisit.models import NewVisit
AppointmentTypes = (
                        ('New Visit','New Visit'),
                        ('Repeat', 'Repeat'),
                        ('Consultation', 'Consultation'),
                        ('Follow up','Follow up'),
                        ('Operative','Operative')
)

AppointmentStatuss = (
                        ('Waiting','Waiting'),
                        ('On going', 'On going'),
                        ('Done', 'Done'),
                        ('Cancel','Cancel'),
    )


# Create your models here.
class Appointment(models.Model):
    patient= models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, related_name="patient_appointments")
    appointmentDate = models.DateField(null=True, blank=True)
    appointmentType = models.CharField(max_length=20,blank=True, choices=AppointmentTypes)
    appointmentStatus = models.CharField(max_length=20,blank=True, choices=AppointmentStatuss)
    operation = models.ManyToManyField(Operation, blank=False)
    followup = models.ManyToManyField(Followup, blank=False)
    new_visit = models.ManyToManyField(NewVisit, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ('-appointmentDate',)
 
    def __str__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse('home')