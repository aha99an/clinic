from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Patient
from django.urls import reverse_lazy
from .forms import PatientListViewForm
from appointment.models import Appointment
from django.db.models import Q

# Create your views here.


class PatientListView(ListView):
    model = Patient
    template_name = 'patients.html'


    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        print(self.paginate_by)
        return super().dispatch(request, *args, **kwargs)        


    def get_queryset(self):
        queryset = Patient.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(name__contains=search_value)
        queryset = Patient.objects.filter(admin_student_list1)
        return queryset
class AllPatientListView(ListView):
    model = Patient
    template_name = 'allpatients.html'

    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        print(self.paginate_by)
        return super().dispatch(request, *args, **kwargs)        


    def get_queryset(self):
        queryset = Patient.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(name__contains=search_value)
        queryset = Patient.objects.filter(admin_student_list1)
        return queryset
class PatienDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'


    # def get_object(self):
    #     my_patient= Patient.objects.get(id=self.kwargs.get("pk"))
    #     print (self.kwargs.get("pk"))
    #     print (my_patient)
    #     return my_patient

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.filter(patient=self.get_object()).values("operation__operationName")
        print(appointments)
        ctx["alloperations"] = appointments
        return ctx




    # def get_context_data(self):
    #     ctx = super().get_context_data()
    #     ctx["alloperations"] = Appointment.objects.all()
    #     # my_patient
    #     appointments = Appointment.objects.filter(patient=my_patient).values_list("operation__operationName")
    #     for appointment in appointments:
    #         appointment.operations.all().values_list("")
    #     # Appointment.objects.all()
    #     Appointment.objects.values("appointmentType")
    #     ctx["hello"] = {patient1: operation1, pat}
    #     return ctx

    # def get_context_data(self):
    #     ctx = super().get_context_data()
    #     ctx["alloperations"] = Appointment.objects.filter()
    #     #  Appointment.objects.all()
    #     ctx["hello"] = "yasser"
    #     return ctx

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


      