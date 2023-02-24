from django.shortcuts import get_object_or_404, render, redirect
from .models import Agent, Lead
from .forms import LeadModelForm


def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/lead_list.html', {
        'leads': leads,
    })


def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads/lead_detail.html', {
        'lead': lead,
    })


def lead_create(request):
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    form = LeadModelForm()
    return render(request, 'leads/lead_create.html', {
        'form': form,
    })
