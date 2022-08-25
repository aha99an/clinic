from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Patient
from django.urls import reverse_lazy
from .forms import PatientListViewForm
from appointment.models import Appointment
# Create your views here.


class PatientListView(ListView):
    model = Patient
    template_name = 'patients.html'

    # def get_context_data(self):
    #     ctx = super().get_context_data()
    #     ctx["alloperations"] = Appointment.objects.filter()
    #     #  Appointment.objects.all()
    #     ctx["hello"] = "yasser"
    #     return ctx

class PatienDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'



class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientListViewForm
    template_name = 'patient_new.html'
    # fields = ('name', 'phoneNumber', 'birthdate','gender','patientAddress','referredFrom','cause','diagnose','investigation','attachment','note')


class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient_edit.html'
    form_class = PatientListViewForm

    # fields = ['name', 'phoneNumber', 'birthdate' ,'gender','patientAddress','cause','diagnose','investigation','treatment','referredFrom','note']




class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient_delete.html'
    success_url = reverse_lazy('patients')
    
#class AttachmentDetailView(DetailView):
  #  model = Patient
 #   template_name = 'attachments.html'