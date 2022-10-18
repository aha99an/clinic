"""clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include # new
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # new
    path('patients/', include('patient.urls')), # new
    path('referrers/', include('referrer.urls')), # new
    path('causes/', include('cause.urls')), # new
    path('investigations/', include('investigation.urls')), # new
    path('diagnose/', include('diagnose.urls')), # new
    path('operation/', include('operation.urls')), # new
    path('treatment/', include('treatment.urls')), # new
    path('appointment/', include('appointment.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('followup/', include('followup.urls')), # new
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

