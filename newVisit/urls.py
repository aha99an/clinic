from django.urls import path
from .views import NewVisitCreateView, NewVisitDeleteView, NewVisitListView, NewVisitUpdateView

urlpatterns = [
path('', NewVisitListView.as_view(), name='newVisits'),
path('newVisit/new/', NewVisitCreateView.as_view(), name='newVisit_new'),
path('newVisit/<int:pk>/edit/', NewVisitUpdateView.as_view(), name='newVisit_edit'),
path('newVisit/<int:pk>/delete/',  NewVisitDeleteView.as_view(), name='newVisit_delete'),

]