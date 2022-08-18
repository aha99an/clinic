from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Appointment
from patient.models import Patient 
from operation.models import Operation
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import AddAppointment
# Create your views here.

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments.html'

    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        print(self.paginate_by)
        return super().dispatch(request, *args, **kwargs)        

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AddAppointment
    template_name = 'appointment_new.html'



class AppointmentUpdateView(UpdateView):
    model = Appointment
    template_name = 'appointment_edit.html'
    fields = ['patient', 'appointmentDate','appointmentType','appointmentStatus','appointmentStatus','operation']



class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment_delete.html'
    success_url = reverse_lazy('appointments')