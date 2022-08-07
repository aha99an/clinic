from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.views.generic.edit import DeleteView
from .models import Patient
# Create your views here.


class PatientListView(ListView):
    model = Patient
    template_name = 'patients.html'


class PatienDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'

#class AttachmentDetailView(DetailView):
  #  model = Patient
 #   template_name = 'attachments.html'