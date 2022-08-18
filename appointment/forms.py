from django import forms
from .models import Appointment
from patient.models import Patient
from operation.models import Operation

class AddAppointment(forms.ModelForm):
    patient= forms.ModelChoiceField( queryset=Patient.objects.all(),label="Patient")
    appointmentDate = forms.DateField(label="Appointment date", widget=forms.DateInput(format='%Y-%m-%d'))
    appointmentType = forms.CharField(label="Appointmen type")
    appointmentStatus = forms.CharField(label="Appointment Status")
    operation = forms.ModelMultipleChoiceField(queryset=Operation.objects.all(),label="Operation")
    
    
    
    
    
    
    
    

    class Meta:
        model = Appointment
        fields = ('patient', 'appointmentDate', 'appointmentType','appointmentStatus','operation')