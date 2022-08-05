from django.db import models
from patient.models import Patient

# Create your models here.
class appointment(models.Model):
    patient= models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True)
    appointmentDate = models.DateField(null=True, blank=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

