from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Appointment
from patient.models import Patient 
from operation.models import Operation
from django.urls import reverse_lazy
from django.db.models import Q
import csv 
from .forms import AppointmentCreateViewForm
from django.http import HttpResponse
# Create your views here.



def import_csvappo(request):
    # Investigation.objects.all().delete()
    with open('/home/ahmed/Desktop/Clinic_project/clinic/csv files/app.csv', 'r', encoding='utf-16') as file:
        reader = csv.reader(file)
        # Patient.objects.all().delete()
        x=0
        for row in reader:
            mypat, _ = Patient.objects.get_or_create(
                name=row[0],
                birthdate = row[1]
            )
            # mypat = Patient.objects.get(
            #     name = row[0],
            #     )
            myappo = Appointment.objects.create(
                patient = mypat,
                appointmentDate = row[1],
                appointmentType = row[2],
                appointmentStatus = row[3],
                ) 
            # myappo.patient.add(mypat)
            # print (myappo)
            x=x+1
            # print (x)
         
    return HttpResponse('Import done')



class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments.html'

    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        # print(self.paginate_by)
        return super().dispatch(request, *args, **kwargs)        




    def get_queryset(self):
        queryset = Appointment.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(patient__name__contains=search_value)
        queryset = Appointment.objects.filter(admin_student_list1)
        return queryset
class AppointmentCreateView(CreateView):
    # model = Appointment
    form_class = AppointmentCreateViewForm
    template_name = 'appointment_new.html'


  #  def get_context_data(self):
   #     ctx = super().get_context_data()
    #    ctx["operations"] = Operation.objects.all()
     #   return ctx




class AppointmentUpdateView(UpdateView):
    form_class = AppointmentCreateViewForm
    model = Appointment
    template_name = 'appointment_edit.html'
    # fields = ['patient', 'appointmentDate','appointmentType','appointmentStatus','appointmentStatus','operation']
    # def get_context_data(self):
    #     ctx = super().get_context_data()
    #     ctx["hello"] = "hiiii"
    #     return ctx


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment_delete.html'
    success_url = reverse_lazy('appointments')



class AppointmentsPatientDetailView(ListView):
    model = Appointment
    template_name = 'appointments_for_Patient.html'
    def get_object(self):
        my_patient = Patient.objects.get(id = self.kwargs.get("pk"))
        return my_patient



    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        my__patient = self.get_object()
        ctx["appointmentsforpatient"] = Appointment.objects.filter(patient_id = my__patient.id)
        ctx["my__patient_id"] = my__patient.id        
        ctx["my__patient"] = my__patient 
       
        return ctx



