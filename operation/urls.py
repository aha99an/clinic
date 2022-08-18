from django.urls import path
from .views import OperationCreateView, OperationDeleteView, OperationListView, OperationUpdateView

urlpatterns = [
path('', OperationListView.as_view(), name='operations'),
path('operation/new/', OperationCreateView.as_view(), name='operation_new'),
path('operation/<int:pk>/edit/', OperationUpdateView.as_view(), name='operation_edit'),
path('operation/<int:pk>/delete/',  OperationDeleteView.as_view(), name='operation_delete'),

]