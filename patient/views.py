from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.http import HttpResponse
from .models import Patient , Attachment
from django.urls import reverse_lazy
from .forms import PatientListViewForm
from appointment.models import Appointment
from django.db.models import Q
import csv 
from datetime import date
import ast
from cause.models import Cause
from referrer.models import Referrer
from diagnose.models import Diagnose
from investigation.models import Investigation
from treatment.models import Treatment
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.base import ContentFile
from io import StringIO
from PIL import Image as PilImage
import os

class PatientListView(ListView):
    model = Patient
    template_name = 'patients.html'


    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        return super().dispatch(request, *args, **kwargs)        


    def get_queryset(self):
        global queryset
        queryset = Patient.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        if search_value:
            admin_student_list1 = Q(name__icontains=search_value)
            admin_student_list2 = Q(diagnose__diagnoseName__icontains=search_value)
            admin_student_list3 = Q(patient_appointments__operation__operationName__icontains=search_value)
            queryset = Patient.objects.filter(admin_student_list1 | admin_student_list2 | admin_student_list3).distinct()
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
        admin_student_list1 = Q(name__icontains=search_value)
        queryset = Patient.objects.filter(admin_student_list1)
        return queryset
class PatienDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.filter(patient=self.get_object()).values("operation__operationName")
        ctx["alloperations"] = appointments
        return ctx

    # def get_object(self):
    #     my_patient= Patient.objects.get(id=self.kwargs.get("pk"))
    #     print (self.kwargs.get("pk"))
    #     print (my_patient)
    #     return my_patient


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
    
class AttachmentDetailView(DetailView):
   model = Patient
   template_name = 'attachments.html'

def delete_image (request, id): 
    image = Attachment.objects.get(id=id).delete()
    return  HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def rotate_Left(request,id):
    myimage = Attachment.objects.get(id=id)
    im = PilImage.open(image.image)
    rotated_image = im.rotate(270)
    rotated_image.save(item.image.file.name, overwrite=True)

  
    # Attachment.objects.create(
    #         patient_id=int(mypatient), attachment=f, id=id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def uploadAttachment(request):
    files = request.FILES.getlist('attachment')
    # print (form)
    # print (request.FILES.getlist('attachment'))
    mypatient = request.POST['patient_pk']
    # print (request.POST['patient_pk'])

    # print ('0000000000000000000000000000000000000000')
    for f in files:
        Attachment.objects.create(
            patient_id=int(mypatient), attachment=f)
    return redirect(f'patient/{mypatient}/attachments/')

def Export_csv(request):
    # print('ddddddddddddddddddddddddd')
    # print (queryset)
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachmet; filename = Patient' + str(date.today())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Name','Phone number','Years','Months','Gender','Patient address','Causes','Diagnoses','Investigations','Treatments','Operations'])
    for patient in queryset:
        # referred = list( patient.referredFrom.all().values_list('referrerName', flat=True))
        cause = list( patient.cause.all().values_list('causeName', flat=True))
        diagnose = list( patient.diagnose.all().values_list('diagnoseName', flat=True))
        investigation = list( patient.investigation.all().values_list('investigationName', flat=True))
        treatment = list( patient.treatment.all().values_list('treatmentName', flat=True))
        operations = list( Appointment.objects.filter(patient = patient, appointmentType = 'Operative').values_list('operation__operationName', flat=True))
        writer.writerow([patient.name, patient.phoneNumber, patient.years, patient.months, patient.gender, 
            patient.patientAddress, cause, diagnose, investigation,treatment, operations])

    return response

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../csv_files/last_update/all_data patients-2022-10-20.csv')


def import_csvpat(request):
    Patient.objects.all().delete()
    Referrer.objects.all().delete()
    Investigation.objects.all().delete()
    Cause.objects.all().delete()
    Diagnose.objects.all().delete()
    Treatment.objects.all().delete()


    with open(filename, 'r', encoding='utf-16') as file:
        reader = csv.reader(file)
        x=0
        for row in reader:
            x=x+1
            patientName= row[0]
            

            mypatient, _ = Patient.objects.get_or_create(
                name=patientName,
                phoneNumber = '0' + row[4],
                birthdate = row[1],
                gender = row[3],
                patientAddress = row[5],
                note = row[9],
                patientComplaint = row[7]
                ) 
            referredFrom_str = row[6]
            referredFrom_name= ast.literal_eval(referredFrom_str)
            for referredFrom5 in referredFrom_name:
                referrer, _ = Referrer.objects.get_or_create(referrerName=referredFrom5)
                mypatient.referredFrom.add(referrer)
           
            cause_str = row[10]
            cause_name= ast.literal_eval(cause_str)
            for cause5 in cause_name:
                cause, _ = Cause.objects.get_or_create(causeName=cause5)
                mypatient.cause.add(cause)


            diagnose_str = row[11]
            diagnose_name= ast.literal_eval(diagnose_str)
            for diagnose5 in diagnose_name:
                diagnose, _ = Diagnose.objects.get_or_create(diagnoseName=diagnose5)
                mypatient.diagnose.add(diagnose)

            # investigation_str = row[8]
            # investigation_name= ast.literal_eval(diagnose_str)
            # for investigation5 in investigation_name:
            #     investigation, _ = Investigation.objects.get_or_create(investigationName=diagnose5)
            #     mypatient.investigation.add(investigation)


            treatment_str = row[12]
            treatment_name= ast.literal_eval(treatment_str)
            for treatment5 in treatment_name:
                treatment, _ = Treatment.objects.get_or_create(treatmentName=treatment5)
                mypatient.treatment.add(treatment)
            print (x)
            print (mypatient)
    return HttpResponse('Import done')