from django.contrib import admin

# Register your models here.
from .models import Patient, Attachment

admin.site.register(Patient)
admin.site.register(Attachment)

