from django.urls import path
from .views import CauseCreateView, CauseDeleteView, CauseListView, CauseUpdateView

urlpatterns = [
path('causes', CauseListView.as_view(), name='causes'),
path('cause/new/', CauseCreateView.as_view(), name='cause_new'),
path('cause/<int:pk>/edit/', CauseUpdateView.as_view(), name='cause_edit'),
path('cause/<int:pk>/delete/',  CauseDeleteView.as_view(), name='cause_delete'),

]