from django.views import generic
from django.shortcuts import reverse, get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from leads.models import Agent, UserProfile
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin

User = get_user_model()


class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        current_user = self.request.user
        current_userprofile = get_object_or_404(UserProfile, user=current_user)
        return get_list_or_404(Agent, organisation=current_userprofile)


class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.filter(organisation=self.request.user.userprofile)


class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent_list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save()
        Agent.objects.create(
            user=user, organisation=self.request.user.userprofile
        )
        send_mail(
            subject="You are invited to be an agent.",
            message="You were added as an agent. Please login to start working.",
            from_email="test@test.com",
            recipient_list=[user.email],
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"

    def get_success_url(self):
        return reverse("agents:agent_list")

    def get_queryset(self):
        current_user = self.request.user
        current_userprofile = get_object_or_404(UserProfile, user=current_user)
        return get_list_or_404(Agent, organisation=current_userprofile)


class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent_list")

    def get_queryset(self):
        current_user = self.request.user
        current_userprofile = get_object_or_404(UserProfile, user=current_user)
        return get_list_or_404(Agent, organisation=current_userprofile)
