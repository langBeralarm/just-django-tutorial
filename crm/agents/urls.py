from django.urls import path
from .views import (
    AgentListView,
    AgentDetailView,
    AgentCreateView,
    AgentDeleteView,
)

app_name = "agents"

urlpatterns = [
    path("", AgentListView.as_view(), name="agent_list"),
    path("<int:pk>", AgentDetailView.as_view(), name="agent_detail"),
    path("create/", AgentCreateView.as_view(), name="agent_create"),
    path("<int:pk>/delete", AgentDeleteView.as_view(), name="agent_delete"),
]
