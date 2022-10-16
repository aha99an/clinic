from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Cause

# Create your views here.


class CauseListView(ListView):
    model = Cause
    template_name = 'causes.html'
    

    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        return super().dispatch(request, *args, **kwargs)        
        
    def get_queryset(self):
        queryset = Cause.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(causeName__icontains=search_value)
        queryset = Cause.objects.filter(admin_student_list1)
        return queryset

class CauseCreateView(CreateView):
    model = Cause
    template_name = 'cause_new.html'
    fields = ['causeName']


class CauseUpdateView(UpdateView):
    model = Cause
    template_name = 'cause_edit.html'
    fields = ['causeName']



class CauseDeleteView(DeleteView):
    model = Cause
    template_name = 'cause_delete.html'
    success_url = reverse_lazy('causes')