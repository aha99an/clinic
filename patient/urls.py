from django.urls import path
from .views import PatientListView, PatienDetailView
#,AttachmentDetailView





urlpatterns = [
path('patients', PatientListView.as_view(), name='patients'),
path('patient/<int:pk>/', PatienDetailView.as_view(), name='patient_detail'),
#path('patient/<int:pk>/attachments', AttachmentDetailView.as_view(), name='attachments.html'), # new

]