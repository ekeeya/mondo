from django.shortcuts import render
from django.conf import settings


# Create your views here.

def index(request):
    template_name = 'landing/index.haml'
    context = dict(STATIC_URL=settings.STATIC_URL)
    # Nyondwa Paul
    return render(request, template_name, context)
