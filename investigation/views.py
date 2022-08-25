from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Investigation
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

class InvestigationListView(ListView):
    model = Investigation
    template_name = 'investigations.html'
    

    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        print(self.paginate_by)
        return super().dispatch(request, *args, **kwargs)        
        
    def get_queryset(self):
        queryset = Investigation.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(investigationName__contains=search_value)
        queryset = Investigation.objects.filter(admin_student_list1)
        return queryset

class InvestigationCreateView(CreateView):
    model = Investigation
    template_name = 'investigation_new.html'
    fields = ['investigationName']


class InvestigationUpdateView(UpdateView):
    model = Investigation
    template_name = 'investigation_edit.html'
    fields = ['investigationName']



class InvestigationDeleteView(DeleteView):
    model = Investigation
    template_name = 'investigation_delete.html'
    success_url = reverse_lazy('investigations')