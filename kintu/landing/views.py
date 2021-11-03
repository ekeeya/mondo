"""
Mondo v 1.0
Created by Keeya Emmanuel  on 01-August-2021

"""

from django.shortcuts import render
from django.conf import settings


def index(request):
    template_name = 'landing/index.haml'
    context = dict(STATIC_URL=settings.STATIC_URL)
    return render(request, template_name, context)
