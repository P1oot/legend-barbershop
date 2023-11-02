from django.shortcuts import render
from .models import Services, Haircuts, Promotions


def index(request):
    template = 'index.html'
    services_list = Services.objects.all()
    haircut_list = Haircuts.objects.all()
    promotions_list = Promotions.objects.all()
    context = {
        'services': services_list,
        'haircuts': haircut_list,
        'promotions': promotions_list
    }
    return render(request, template, context)
