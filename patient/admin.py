from django.contrib import admin

# Register your models here.
from .models import Patient, Attachment




class PatientAdmin(admin.ModelAdmin):
    class Meta:
        model = Patient

 
    readonly_fields = ( 'created_at', 'updated_at')

admin.site.register(Patient,PatientAdmin)
admin.site.register(Patient)
admin.site.register(Attachment)

