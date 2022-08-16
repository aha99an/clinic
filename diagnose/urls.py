from django.urls import path
from .views import DiagnoseCreateView, DiagnoseDeleteView, DiagnoseListView, DiagnoseUpdateView

urlpatterns = [
path('diagnoses', DiagnoseListView.as_view(), name='diagnoses'),
path('diagnose/new/', DiagnoseCreateView.as_view(), name='diagnose_new'),
path('diagnose/<int:pk>/edit/', DiagnoseUpdateView.as_view(), name='diagnose_edit'),
path('diagnose/<int:pk>/delete/',  DiagnoseDeleteView.as_view(), name='diagnose_delete'),

]