from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent, UserProfile
from .forms import AgentModelForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        current_user = self.request.user
        current_userprofile = UserProfile.objects.get(user=current_user)
        return Agent.objects.filter(organisation=current_userprofile)


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        current_user = self.request.user
        current_userprofile = UserProfile.objects.get(user=current_user)
        return Agent.objects.filter(organisation=current_userprofile)


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent_list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user
        agent.save()
        super(AgentModelForm, self).form_valid(form)


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"

    def get_success_url(self):
        return reverse("agents:agent_list")

    def get_queryset(self):
        current_user = self.request.user
        current_userprofile = UserProfile.objects.get(user=current_user)
        return Agent.objects.filter(organisation=current_userprofile)


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent_list")

    def get_queryset(self):
        current_user = self.request.user
        current_userprofile = UserProfile.objects.get(user=current_user)
        return Agent.objects.filter(organisation=current_userprofile)
