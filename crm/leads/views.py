from django.shortcuts import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead
from .forms import LeadModelForm, CustomUserCreationForm
from agents.mixins import OrganisorAndLoginRequiredMixin


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation
            )
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation
            )
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadCreateView(OrganisorAndLoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="See the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"],
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(OrganisorAndLoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)


class LeadDeleteView(OrganisorAndLoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead_list")

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)
