from django import forms
from .models import Patient, GENDER, Attachment
from referrer.models import Referrer
from cause.models import Cause
from diagnose.models import Diagnose
from investigation.models import Investigation
from django.contrib.admin.widgets import FilteredSelectMultiple    
from django.core.validators import MaxValueValidator, MinValueValidator

from treatment.models import Treatment


def check_size(value):
    if len(value) < 11 and value.isdigit():
        raise forms.ValidationError("Phone number is not correct")
class PatientListViewForm(forms.ModelForm):
    name = forms.CharField(max_length=255,label= "Patient name")
    phoneNumber =forms.CharField(validators=[check_size, ], label="Phone number", required=False)
    # birthdate = forms.DateField(label="Birthdate", widget=forms.DateInput(format='%Y-%m-%d'))
    # birthdate = forms.DateField(label="Birthdate", widget = forms.HiddenInput(), required=False)
    days = forms.IntegerField(validators=[MaxValueValidator(365),MinValueValidator(0)])
    months = forms.IntegerField(validators=[MaxValueValidator(12),MinValueValidator(0)])
    years = forms.IntegerField(validators=[MaxValueValidator(200),MinValueValidator(0)])
    gender = forms.ChoiceField(choices=GENDER, label="Gender")
    patientAddress = forms.CharField(label="Patient address", required=False)
    patientComplaint = forms.CharField(label="Patient complaint", required=False)
    referredFrom = forms.ModelMultipleChoiceField(required=False, queryset = Referrer.objects.all(), label="Referred from",
                initial=[Referrer.objects.all().values_list("referrerName", flat=True)])
    
    cause = forms.ModelMultipleChoiceField(required=False, queryset = Cause.objects.all(), label="Causes",
                initial=[Cause.objects.all().values_list("causeName", flat=True)])
    
    diagnose = forms.ModelMultipleChoiceField(required=False, queryset = Diagnose.objects.all(), label="Diagnoses",
                initial=[Diagnose.objects.all().values_list("diagnoseName", flat=True)])
    
    investigation = forms.ModelMultipleChoiceField(required=False, queryset = Investigation.objects.all(), label="Investigations",
                initial=[Investigation.objects.all().values_list("investigationName", flat=True)])

    treatment = forms.ModelMultipleChoiceField(required=False, queryset = Treatment.objects.all(), label="Treatments",
                initial=[Treatment.objects.all().values_list("treatmentName", flat=True)])

    note = forms.CharField(widget=forms.Textarea, label="Notes", required=False)
    
    
    
    
    def __init__(self, *args, **kwargs):
        super(PatientListViewForm, self).__init__(*args, **kwargs)
        # breakpoint()
        if self.instance.birthdate != None:
            self.fields['days'].initial = self.instance.days
            self.fields['months'].initial = self.instance.months
            self.fields['years'].initial = self.instance.years
        else:
            self.fields['days'].initial = 0
            self.fields['months'].initial = 0
            # self.fields['years'].initial = self.instance.years
        for visible in self.visible_fields():
            if visible.name in ["referredFrom","cause","diagnose","investigation","treatment"]:
                # print(visible.field._queryset)
                visible.field.widget.attrs["class"] = 'js-example-basic-multiple'
                visible.field.widget.attrs["name"] = 'states[]'
                visible.field.widget.attrs["multiple"] = 'multiple'

    class Meta:
        model = Patient
        fields = ('name', 'phoneNumber','days','months','years','gender','patientAddress','patientComplaint','referredFrom','cause','diagnose','investigation',"treatment",'note')

     

class AttachmentView(forms.Form):
    attachment = forms.FileField(label="Attachment", required=False ,widget=forms.ClearableFileInput(attrs={'multiple': True}))
    # class Meta:
    #     model = Attachment
    #     fields = ('attachment',)