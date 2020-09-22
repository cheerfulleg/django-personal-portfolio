from django.shortcuts import render

from .models import Project


def home(request):
    context = {
        'projects': Project.objects.all().order_by('-id')[:8],
    }
    return render(request, 'portfolio/home.html', context)
