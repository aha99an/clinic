from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from django.views.generic.edit import DeleteView
from .models import Patient
# Create your views here.


class PatientView(ListView):
    model = Patient
    template_name = 'patients.html'