from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Treatment

# Create your views here.


class TreatmentListView(ListView):
    model = Treatment
    template_name = 'treatments.html'
    

    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        # print(self.paginate_by)
        return super().dispatch(request, *args, **kwargs)        
        
    def get_queryset(self):
        queryset = Treatment.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(treatmentName__contains=search_value)
        queryset = Treatment.objects.filter(admin_student_list1)
        return queryset

class TreatmentCreateView(CreateView):
    model = Treatment
    template_name = 'treatment_new.html'
    fields = ['treatmentName']


class TreatmentUpdateView(UpdateView):
    model = Treatment
    template_name = 'treatment_edit.html'
    fields = ['treatmentName']



class TreatmentDeleteView(DeleteView):
    model = Treatment
    template_name = 'treatment_delete.html'
    success_url = reverse_lazy('treatments')