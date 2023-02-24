from django.urls import path
from .views import lead_create, lead_detail, lead_list, lead_update

app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='lead_list'),
    path('<int:pk>/', lead_detail, name='lead_detail'),
    path('<int:pk>/update/', lead_update, name='lead_update'),
    path('create/', lead_create, name='lead_create'),
]
