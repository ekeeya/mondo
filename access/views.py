from django.shortcuts import render


# Create your views here.

def index(request):
    template_name = 'skin/index.haml'
    return render(request, template_name)
