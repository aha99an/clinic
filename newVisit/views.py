from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import NewVisit
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

class NewVisitListView(ListView):
    model = NewVisit
    template_name = 'newVisits.html'
    

    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        return super().dispatch(request, *args, **kwargs)        
        
    def get_queryset(self):
        queryset = NewVisit.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(newVisitName__icontains=search_value)
        queryset = NewVisit.objects.filter(admin_student_list1)
        return queryset

class NewVisitCreateView(CreateView):
    model = NewVisit
    template_name = 'newVisit_new.html'
    fields = ['newVisitName']


class NewVisitUpdateView(UpdateView):
    model = NewVisit
    template_name = 'newVisit_edit.html'
    fields = ['newVisitName']



class NewVisitDeleteView(DeleteView):
    model = NewVisit
    template_name = 'newVisit_delete.html'
    success_url = reverse_lazy('newVisit')