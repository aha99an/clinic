





from django.urls import path
from .views import AppointmentCreateView, AppointmentDeleteView, AppointmentListView, AppointmentUpdateView

urlpatterns = [
path('appointments', AppointmentListView.as_view(), name='appointments'),
path('appointment/new/', AppointmentCreateView.as_view(), name='appointment_new'),
path('appointment/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_edit'),
path('appointment/<int:pk>/delete/',  AppointmentDeleteView.as_view(), name='appointment_delete'),

]