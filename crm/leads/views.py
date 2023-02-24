from django.shortcuts import get_object_or_404, render, redirect
from .models import Lead
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
