from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Followup
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

class FollowupListView(ListView):
    model = Followup
    template_name = 'followups.html'
    

    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        return super().dispatch(request, *args, **kwargs)        
        
    def get_queryset(self):
        queryset = Followup.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(followupName__icontains=search_value)
        queryset = Followup.objects.filter(admin_student_list1)
        return queryset

class FollowupCreateView(CreateView):
    model = Followup
    template_name = 'followup_new.html'
    fields = ['followupName']


class FollowupUpdateView(UpdateView):
    model = Followup
    template_name = 'followup_edit.html'
    fields = ['followupName']



class FollowupDeleteView(DeleteView):
    model = Followup
    template_name = 'followup_delete.html'
    success_url = reverse_lazy('followups')