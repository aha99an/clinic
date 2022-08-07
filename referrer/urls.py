from django.urls import path
from .views import ReferrerCreateView, ReferrerDeleteView, ReferrerListView, ReferrerUpdateView

urlpatterns = [
path('referrers', ReferrerListView.as_view(), name='referrers'),
path('referrer/new/', ReferrerCreateView.as_view(), name='referrer_new'),
path('referrer/<int:pk>/edit/', ReferrerUpdateView.as_view(), name='referrer_edit'),
path('referrer/<int:pk>/delete/',  ReferrerDeleteView.as_view(), name='referrer_delete'),

]