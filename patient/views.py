from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Patient
from django.urls import reverse_lazy
# Create your views here.


class PatientListView(ListView):
    model = Patient
    template_name = 'patients.html'


class PatienDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'



class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patient_new.html'
    fields = ['name', 'phoneNumber', 'birthdate' ,'gender','patientAddress','referredFrom','note']


class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient_edit.html'
    fields = ['name', 'phoneNumber', 'birthdate' ,'gender','patientAddress','referredFrom','note']




class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient_delete.html'
    success_url = reverse_lazy('patients')
    
#class AttachmentDetailView(DetailView):
  #  model = Patient
 #   template_name = 'attachments.html'