from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Lead
from .forms import LeadModelForm


def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    return render(request, 'leads/lead_update.html', {
        'form': form,
        'lead': lead,
    })


def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead.delete()
    return redirect('/leads')


class LeadListView(ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')
