from django import forms
from .models import Patient, GENDER
from referrer.models import Referrer
from cause.models import Cause
from diagnose.models import Diagnose
from investigation.models import Investigation
#from treatment.models import treatment


def check_size(value):
    if len(value) < 11 and value.isdigit():
        raise forms.ValidationError("Phone number is not correct")


class PatientListViewForm(forms.ModelForm):
    name = forms.CharField(max_length=255,label= "Patient name")
    phoneNumber =forms.CharField(validators=[check_size, ], label="Phone number", required=False)
    birthdate = forms.DateField(label="Birthdate", widget=forms.DateInput(format='%Y-%m-%d'))
    gender = forms.ChoiceField(choices=GENDER, label="Gender")
    patientAddress = forms.CharField(label="Patient address", required=False)
    # referredFrom = forms.ModelChoiceField(queryset=Referrer.objects.all(),label="Referred from", required=False)
    cause = forms.ModelChoiceField(queryset=Cause.objects.all(),label="Cause", required=False)
    # diagnose = forms.ModelChoiceField(queryset=Diagnose.objects.all(),label="Diagnose", required=False)
    # investigation = forms.ModelChoiceField(queryset=Investigation.objects.all(),label="Investigation", required=False)
    # #treatment = forms.ModelChoiceField(queryset=treatment.objects.all(),label="Treatment")
    # attachment = forms.FileField(label="Attachment", required=False)
    note = forms.CharField(widget=forms.Textarea, label="Notes", required=False)    

    class Meta:
        model = Patient
        fields = ('name', 'phoneNumber', 'birthdate','gender','patientAddress','referredFrom','cause','diagnose','investigation','attachment','note')
     