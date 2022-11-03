from django.urls import path
from .views import FollowupCreateView, FollowupDeleteView, FollowupListView, FollowupUpdateView

urlpatterns = [
path('', FollowupListView.as_view(), name='followups'),
path('followup/new/', FollowupCreateView.as_view(), name='followup_new'),
path('followup/<int:pk>/edit/', FollowupUpdateView.as_view(), name='followup_edit'),
path('followup/<int:pk>/delete/',  FollowupDeleteView.as_view(), name='followup_delete'),

]