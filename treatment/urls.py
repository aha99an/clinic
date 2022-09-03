from django.urls import path
from .views import TreatmentCreateView, TreatmentDeleteView, TreatmentListView, TreatmentUpdateView

urlpatterns = [
path('', TreatmentListView.as_view(), name='treatments'),
path('treatment/new/', TreatmentCreateView.as_view(), name='treatment_new'),
path('treatment/<int:pk>/edit/', TreatmentUpdateView.as_view(), name='treatment_edit'),
path('treatment/<int:pk>/delete/',  TreatmentDeleteView.as_view(), name='treatment_delete'),

]