from django.urls import path
from .views import lead_delete, LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete', lead_delete, name='lead_delete'),
    path('create/', LeadCreateView.as_view(), name='lead_create'),
]
