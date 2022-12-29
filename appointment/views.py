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
import os
from operation.models import Operation
import ast
# Create your views here.


def import_csvappo(request):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../csv_files/last_update/appointments.csv')
    errors_filename = os.path.join(dirname, '../csv_files/last_update/appointment-2022-10-20_errors.csv')
    with open(filename, 'r', encoding='utf-16') as file, open(errors_filename, 'w', encoding='utf-16') as errors_file:
        reader = csv.reader(file)
        writer = csv.writer(errors_file)
        Appointment.objects.all().delete()
        x=0
        for row in reader:
            try:
                mypat= Patient.objects.get(name=row[0].capitalize())
                # print ("000000000000000000000000000000000000000")
                # print ("000000000000000000000000000000000000000")
                # print (mypat)
                myappo = Appointment.objects.create(
                    patient = mypat,
                    appointmentDate = row[1],
                    appointmentType = row[2],
                    appointmentStatus = row[3],
                    )                 
                # myappo.patient.add(mypat)
                # print (myappo)
                x=x+1
                print (x)
            except Exception as e:
                print("111111111111111111111111111111111111111111111111111111111111")
                row.insert(0, e)
                writer.writerow(row)
    return HttpResponse('Import done')


def import_csvAppoForOperation(request):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../csv_files/last_update/patients_operation.csv')
    errors_filename = os.path.join(dirname, '../csv_files/last_update/appointment-2022-10-20_errors.csv')
    with open(filename, 'r', encoding='utf-16') as file, open(errors_filename, 'w', encoding='utf-16') as errors_file:
        reader = csv.reader(file)
        writer = csv.writer(errors_file)
        x=0
        for row in reader:
            try:
                mypat= Patient.objects.get(name=row[0].capitalize())
                myappo = Appointment.objects.create(
                    patient = mypat,
                    appointmentDate = row[8],
                    appointmentType = "Operative",
                    appointmentStatus = "Done",
                    )      
                operation_str = row[13]
                operation_name= ast.literal_eval(operation_str)
                for operation5 in operation_name:
                    operation, _ = Operation.objects.get_or_create(operationName=operation5)
                    myappo.operation.add(operation)         
                # myappo.patient.add(mypat)
                # print (myappo)
                x=x+1
                print (x)
            except Exception as e:
                print("111111111111111111111111111111111111111111111111111111111111")
                row.insert(0, e)
                writer.writerow(row)
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
        # Search by name 
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(patient__name__icontains=search_value)
        queryset = Appointment.objects.filter(admin_student_list1)

        # Search by date 
        search_date = self.request.GET.get('search_date')
        print (search_date)
        
        if search_date== '':
            search_date = None
        else: 
            search_date= search_date
        if search_date== None:
            queryset = queryset
        else: 
            if len(search_date) == 7 or  len(search_date) == 6:
                my_search_date = search_date.split("-")
                my_search_year = my_search_date[1]
                my_search_mounth =  my_search_date[0]
                
                queryset = queryset.filter(appointmentDate__year=my_search_year, appointmentDate__month=my_search_mounth)
            elif len(search_date) > 7 : 
                my_search_date = search_date.split("-")
                my_search_year = my_search_date[2]
                my_search_mounth =  my_search_date[1]
                my_search_day = my_search_date[0]
                queryset = queryset.filter(appointmentDate__year=my_search_year, appointmentDate__month=my_search_mounth, appointmentDate__day=my_search_day)
                    
                    
        # queryset = queryset.filter(appointmentDate__year='2019')
# (date__year='2011', date__month='01')

        # queryset = queryset.filter(appointmentDate=search_date)
        # Filter
        appointmentType = self.request.GET.get('appointmentType')
        if appointmentType:
            if appointmentType == "New Visit":
                queryset = queryset.filter(appointmentType='New Visit')
            elif appointmentType == "Repeat":
                queryset = queryset.filter(appointmentType='Repeat')
            elif appointmentType == "Consultation":
                queryset = queryset.filter(appointmentType='Consultation')
            elif appointmentType == "Follow up":
                queryset = queryset.filter(appointmentType='Follow up')
            elif appointmentType == "Operative":
                queryset = queryset.filter(appointmentType='Operative')

                # Filter
        appointmentStatus = self.request.GET.get('appointmentStatus')
        if appointmentStatus:
            if appointmentStatus == "Waiting":
                queryset = queryset.filter(appointmentStatus='Waiting')
            elif appointmentStatus == "On going":
                queryset = queryset.filter(appointmentStatus='On going')
            elif appointmentStatus == "Done":
                queryset = queryset.filter(appointmentStatus='Done')
            elif appointmentStatus == "Cancel":
                queryset = queryset.filter(appointmentStatus='Cancel')
            
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



