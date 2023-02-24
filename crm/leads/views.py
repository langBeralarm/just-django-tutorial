from django.shortcuts import get_object_or_404, render, redirect
from .models import Agent, Lead
from .forms import LeadForm


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
        form = LeadForm(request.POST)
        if form.is_valid():
            Lead.objects.create(
                first_name=form.data['first_name'],
                last_name=form.data['last_name'],
                age=form.data['age'],
                agent=Agent.objects.all()[0],
                source='YouTube',
            )
            return redirect('/leads')
    form = LeadForm()
    return render(request, 'leads/lead_create.html', {
        'form': form,
    })
