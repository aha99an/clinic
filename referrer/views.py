from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Referrer
from django.urls import reverse_lazy
# Create your views here.

class ReferrerListView(ListView):
    model = Referrer
    template_name = 'referrers.html'


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