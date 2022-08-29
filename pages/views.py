from django.shortcuts import render
from django.views.generic import TemplateView
from appointment.models import Appointment
from django.views.generic import ListView, DetailView
from django.db.models import Q
from datetime import date

class HomePageView(ListView):
    model = Appointment
    template_name = 'home.html'
    def dispatch(self, request, *args, **kwargs):
        self.paginate_by = self.request.POST.get('pagination_num',default=50)
        print(self.paginate_by)
        return super().dispatch(request, *args, **kwargs)        


    def get_queryset(self):
        today = date.today()
        queryset = Appointment.objects.all()
        # Search
        search_value = self.request.GET.get('search_value',default=today)
        admin_student_list1 = Q(appointmentDate__contains=search_value)
        queryset = Appointment.objects.filter(admin_student_list1)
        return queryset



    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        today = date.today()
        today = int(today.strftime('%Y%m%d'))
        today = str(today)
        todaydate = today[0:4] + "-" + today[4:6] + "-" + today[6:8]  
        print (type(todaydate))
        print (todaydate)
        ctx["todaydate"] = todaydate
        return ctx

20220501