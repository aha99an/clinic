from django.contrib import admin

# Register your models here.
from .models import Appointment

admin.site.register(Appointment)


class AppointmentAdmin(admin.ModelAdmin):
    class Meta:
        model = Appointment

 
    readonly_fields = ( 'created_at', 'updated_at')
