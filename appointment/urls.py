from django.urls import path
from .views import AppointmentCreateView, AppointmentDeleteView, AppointmentListView, AppointmentUpdateView, AppointmentsPatientDetailView, import_csvappo

urlpatterns = [
path('', AppointmentListView.as_view(), name='appointments'),
path('appointment/new/', AppointmentCreateView.as_view(), name='appointment_new'),
path('appointment/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_edit'),
path('appointment/<int:pk>/delete/',  AppointmentDeleteView.as_view(), name='appointment_delete'),
path('patient/<int:pk>/appointmentspatient/',  AppointmentsPatientDetailView.as_view(), name='appointments_for_Patient'),
path('import_csvappo',  import_csvappo, name='import-csvappo'),




]