from django.urls import path
from .views import PatientListView, PatienDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView, AllPatientListView, Export_csv, import_csvpat, uploadAttachment, AttachmentDetailView, delete_image, rotate_Left





urlpatterns = [
path('', PatientListView.as_view(), name='patients'),
path('/allpatients', AllPatientListView.as_view(), name='allpatients'),
path('patient/<int:pk>/', PatienDetailView.as_view(), name='patient_detail'),
path('patient/new/', PatientCreateView.as_view(), name='patient_new'),
path('patient/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
path('patient/<int:pk>/delete/',  PatientDeleteView.as_view(), name='patient_delete'),
path('export_csv',  Export_csv, name='export-csv'),
path('import_csvpat',  import_csvpat, name='import-csvpat'),
path('uploadAttachment',  uploadAttachment, name='uploadAttachment'),
path('patient/<int:pk>/attachments/', AttachmentDetailView.as_view(), name='attachments'),

path('delete-image/<int:id>/',  delete_image, name='delete_image'),
path('rotate-Left/<int:id>/',  rotate_Left, name='rotate_Left'),



]
