from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Referrer
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Referrer
# Create your views here.

class ReferrerListView(ListView):
    model = Referrer
    template_name = 'referrers.html'
    paginate_by = 10
    def get_queryset(self):
        queryset = Referrer.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default="")
        admin_student_list1 = Q(
            referrerName__contains=search_value)
        queryset = Referrer.objects.filter(admin_student_list1)
        return queryset

class ReferrerCreateView(CreateView):
    model = Referrer
    template_name = 'referrer_new.html'
    fields = ['referrerName']


class ReferrerUpdateView(UpdateView):
    model = Referrer
    template_name = 'referrer_edit.html'
    fields = ['referrerName']



class ReferrerDeleteView(DeleteView):
    model = Referrer
    template_name = 'referrer_delete.html'
    success_url = reverse_lazy('referrers')