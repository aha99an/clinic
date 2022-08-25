from django import forms
from .models import Appointment, AppointmentStatuss, AppointmentTypes
from patient.models import Patient
from operation.models import Operation


class AppointmentCreateViewForm(forms.ModelForm):
    patient= forms.ModelChoiceField(queryset=Patient.objects.all(),label="Patient")
    appointmentDate = forms.DateField(label="Appointment date", widget=forms.DateInput(format='%Y-%m-%d'))
    appointmentType = forms.ChoiceField(choices=AppointmentTypes, required=False, label="Appointmen type")
    appointmentStatus = forms.ChoiceField(label="Appointment Status", choices=AppointmentStatuss)
    operation = forms.ModelMultipleChoiceField(widget=forms.Select(attrs={
                'class': 'js-example-basic-multiple',
                'name': 'states[]',
                'multiple': 'multiple'
            }), queryset=Operation.objects.all(),label="Operations")
    

    class Meta:
        model = Appointment
        fields = ('patient', 'appointmentDate', 'appointmentType','appointmentStatus','operation')
     