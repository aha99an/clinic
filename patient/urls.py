from django.urls import path
from .views import PatientListView, PatienDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView
#,AttachmentDetailView





urlpatterns = [
path('patients', PatientListView.as_view(), name='patients'),
path('patient/<int:pk>/', PatienDetailView.as_view(), name='patient_detail'),
path('patient/new/', PatientCreateView.as_view(), name='patient_new'),
path('patient/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
path('patient/<int:pk>/delete/',  PatientDeleteView.as_view(), name='patient_delete'),


#path('patient/<int:pk>/attachments', AttachmentDetailView.as_view(), name='attachments.html'), # new

]
