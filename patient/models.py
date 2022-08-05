from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=200, default="0")
    age = models.CharField(max_length=200)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1,blank=True, choices=GENDER)
    YORM = (
        ('Y', 'Year'),
        ('M', 'Month'),
    )
    yORm = models.CharField(max_length=1, blank=True, choices=YORM, verbose_name="Y/M")

    patientAddress = models.CharField(max_length=20000)
    referredFrom = models.CharField(max_length=200)
    attachment = models.FileField(
        null=True, blank=True, verbose_name="attachment")
    investigation = models.FileField(
        null=True, blank=True, verbose_name="investigation")
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name