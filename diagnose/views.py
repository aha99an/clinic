from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Diagnose
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

class DiagnoseListView(ListView):
    model = Diagnose
    template_name = 'diagnoses.html'
    

    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        return super().dispatch(request, *args, **kwargs)        
        
    def get_queryset(self):
        queryset = Diagnose.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(diagnoseName__icontains=search_value)
        queryset = Diagnose.objects.filter(admin_student_list1)
        return queryset

class DiagnoseCreateView(CreateView):
    model = Diagnose
    template_name = 'diagnose_new.html'
    fields = ['diagnoseName']


class DiagnoseUpdateView(UpdateView):
    model = Diagnose
    template_name = 'diagnose_edit.html'
    fields = ['diagnoseName']



class DiagnoseDeleteView(DeleteView):
    model = Diagnose
    template_name = 'diagnose_delete.html'
    success_url = reverse_lazy('diagnoses')