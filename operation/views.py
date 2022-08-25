from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Operation
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

class OperationListView(ListView):
    model = Operation
    template_name = 'operations.html'
    

    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        print(self.paginate_by)
        return super().dispatch(request, *args, **kwargs)        
        
    def get_queryset(self):
        queryset = Operation.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(operationName__contains=search_value)
        queryset = Operation.objects.filter(admin_student_list1)
        return queryset

class OperationCreateView(CreateView):
    model = Operation
    template_name = 'operation_new.html'
    fields = ['operationName']


class OperationUpdateView(UpdateView):
    model = Operation
    template_name = 'operation_edit.html'
    fields = ['operationName']



class OperationDeleteView(DeleteView):
    model = Operation
    template_name = 'operation_delete.html'
    success_url = reverse_lazy('operations')