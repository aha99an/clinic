from django import forms
from .models import Appointment, AppointmentStatuss, AppointmentTypes
from patient.models import Patient
from operation.models import Operation
from django.contrib.admin.widgets import FilteredSelectMultiple    


class AppointmentCreateViewForm(forms.ModelForm):
    patient= forms.ModelChoiceField(queryset=Patient.objects.all(),label="Patient")
    appointmentDate = forms.DateField(label="Appointment date", widget=forms.DateInput(format='%Y-%m-%d'))
    appointmentType = forms.ChoiceField(choices=AppointmentTypes, required=False, label="Appointmen type")
    appointmentStatus = forms.ChoiceField(label="Appointment Status", choices=AppointmentStatuss)
    operation = forms.ModelMultipleChoiceField(required=False, queryset = Operation.objects.all(), label="Operations",
        initial=[Operation.objects.all().values_list("operationName", flat=True)])

    def __init__(self, *args, **kwargs):
        super(AppointmentCreateViewForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == "operation":
                # print(visible.field._queryset)
                visible.field.widget.attrs["class"] = 'js-example-basic-multiple'
                visible.field.widget.attrs["name"] = 'states[]'
                visible.field.widget.attrs["multiple"] = 'multiple'
                


    class Meta:
        model = Appointment
        fields = ('patient', 'appointmentDate', 'appointmentType','appointmentStatus','operation')
     