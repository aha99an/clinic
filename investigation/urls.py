from django.urls import path
from .views import InvestigationCreateView, InvestigationDeleteView, InvestigationListView, InvestigationUpdateView

urlpatterns = [
path('investigations', InvestigationListView.as_view(), name='investigations'),
path('investigation/new/', InvestigationCreateView.as_view(), name='investigation_new'),
path('investigation/<int:pk>/edit/', InvestigationUpdateView.as_view(), name='investigation_edit'),
path('investigation/<int:pk>/delete/',  InvestigationDeleteView.as_view(), name='investigation_delete'),

]