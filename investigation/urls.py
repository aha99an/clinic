from django.urls import path
from .views import InvestigationCreateView, InvestigationDeleteView, InvestigationListView, InvestigationUpdateView, import_csv

urlpatterns = [
path('investigations', InvestigationListView.as_view(), name='investigations'),
path('investigation/new/', InvestigationCreateView.as_view(), name='investigation_new'),
path('investigation/<int:pk>/edit/', InvestigationUpdateView.as_view(), name='investigation_edit'),
path('investigation/<int:pk>/delete/',  InvestigationDeleteView.as_view(), name='investigation_delete'),
path('import_csv',  import_csv, name='import-csv'),

]